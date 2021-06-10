from django.shortcuts import  render, redirect
from .forms import NewCustomerForm, NewRestaurantForm, NewDeliveryExecForm, SearchForm
from django.contrib.auth import login, authenticate,  logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .models import User, Menu, Cart, Customer, Restaurant, addresses, Orders
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
import json
from django.core.serializers.json import DjangoJSONEncoder

class CustomerRegisterView(CreateView):
    model = User
    form_class=NewCustomerForm
    template_name = 'registerCustomer.html'
    def form_valid(self, form):
        user = form.save()
        return redirect('/')
class RestaurantRegisterView(CreateView):
    model = User
    form_class=NewRestaurantForm
    template_name = 'registerRestaurant.html'
    def form_valid(self, form):
        user = form.save()
        return redirect('/')
class DeliveryExecRegisterView(CreateView):
    model = User
    form_class=NewDeliveryExecForm
    template_name = 'registerCustomer.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/permittrack')
def loginview(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                if user.is_delivery:
                    return redirect('/delhome')
                elif user.is_restaurant:
                    return redirect('/resthome')
                return redirect('/home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="loginCustomer.html", context={"login_form":form})
def permittrackview(request):
    if not request.user.is_authenticated or not request.user.is_delivery:
        return redirect('/')
    return render(request=request, template_name="trackDel.html")
class Menulist( UserPassesTestMixin, ListView,LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_restaurant
    model=Menu
    template_name='menu_list.html'
    def get_queryset(self):
        return Menu.objects.filter(restaurant_id=self.request.user)

class AddFood(UserPassesTestMixin, CreateView, LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_restaurant
    model=Menu
    fields = ['food_name','description','food_image','veg','price']
    template_name='updatefood.html'
    def form_valid(self, form):
        form.instance.restaurant_id = self.request.user
        return super().form_valid(form)
    success_url ='/resthome'

class UpdateFood(UserPassesTestMixin, UpdateView, LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_restaurant
    model=Menu
    fields=['food_name','description','food_image','veg','price']
    template_name='updatefood.html'
    success_url='/resthome'
class DeleteFood( UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_restaurant
    model=Menu
    template_name='deletefood.html'
    success_url='/resthome'

class Home( UserPassesTestMixin, ListView,LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_customer
    model=Menu
    template_name='home.html'
    def get_context_data(self, **kwargs):
        con = super(Home, self).get_context_data(**kwargs)
        con['search']=SearchForm()
        return con

class DelHome( UserPassesTestMixin, LoginRequiredMixin, View):
    template_name='homeDel.html'
    def test_func(self):
        return self.request.user.is_delivery
    def get(self, request):
        return render(request, self.template_name, context={'msg': ""})
def takeorderview(request, q=None):
    if not request.user.is_authenticated or not request.user.is_delivery:
        return redirect('/')
    return render(request=request, template_name="deliveryinprocess.html", context={"orderid": q})
class SearchFood( UserPassesTestMixin,ListView,LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_customer
    model=Menu
    template_name='Search.html'
    def get_queryset(self):
        food = self.request.GET.get('search','')
        if not Menu.objects.filter(food_name__icontains=food).exists():
            return None
        object_list=Menu.objects.filter(food_name__icontains=food)
        return object_list

class DetailFood( UserPassesTestMixin, DetailView,LoginRequiredMixin):
    model=Menu
    template_name='Detail.html'
    def test_func(self):
        return self.request.user.is_customer

def additemview(request, pk=None, q=None):
    if not request.user.is_authenticated or not request.user.is_customer:
        return redirect('/')
    item=Menu.objects.get(pk=pk)
    if not Cart.objects.filter(customer_id=request.user, item=item).exists():
        adding= Cart.objects.create(customer_id=request.user, item=item, quantity=q)
        adding.save()
    else:
        update=Cart.objects.get(customer_id=request.user, item=item)
        update.quantity=q
        update.save()
    return redirect('/mycart')

class MyCart(UserPassesTestMixin, ListView, LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_customer
    template_name="Cart.html"
    model=Menu
    def get_queryset(self):
        items=Menu.objects.filter(cart__customer_id=self.request.user).values('food_name', 'price', 'cart')
        print(items)
        object_list=[]
        for obj in items:
            q=Cart.objects.get(pk=obj['cart'])
            object_list.append({'food_name':obj['food_name'], 'price': obj['price'], 'quantity':q.quantity})
        print(object_list)
        return object_list
def ordersummaryview(request):
    if not request.user.is_authenticated or not request.user.is_customer:
        return redirect('/')
    info={}
    cust=Customer.objects.get(user=request.user)
    info['cust_id']=request.user.pk
    info['cust_name']=cust.cus_name
    items=Menu.objects.filter(cart__customer_id=request.user).values('food_name', 'price', 'restaurant_id', 'cart')
    print(items)
    restaurants={}
    for item in items:
        info['rest']=True
        if item['restaurant_id'] not in restaurants:
            restaurants[item['restaurant_id']]={}
            restaurants[item['restaurant_id']]['items']={}
            res=Restaurant.objects.get(pk=item['restaurant_id'])
            restaurants[item['restaurant_id']]['rest_name']=res.res_name
            restaurants[item['restaurant_id']]['pickuplat']=str(res.latitude)
            restaurants[item['restaurant_id']]['pickuplong']=str(res.longitude)
        c=Cart.objects.get(pk=item['cart'])
        restaurants[item['restaurant_id']]['items'][item['food_name']]={}
        restaurants[item['restaurant_id']]['items'][item['food_name']]['price']=item['price']*c.quantity
        restaurants[item['restaurant_id']]['items'][item['food_name']]['quantity']=c.quantity
    print(restaurants)
    return render(request=request, template_name="order.html", context={"info": info, "rests": restaurants})

def orderview(request, q=None):
    if not request.user.is_authenticated or not request.user.is_customer:
        return redirect('/')
    return render(request=request, template_name="orderstatus.html", context={"orderid":q})
def orderlist(request):
    if not request.user.is_authenticated or not request.user.is_restaurant:
        return redirect('/')
    return render(request=request, template_name="orderlist2.html")

def restcheckorderview(request, q=None):
    if not request.user.is_authenticated or not request.user.is_restaurant:
        return redirect('/')
    return render(request=request, template_name="handleOrder.html", context={"orderid":q})
def trackordersview(request):
    if not request.user.is_authenticated or not request.user.is_customer:
        return redirect('/')
    return render(request=request, template_name="orderlist.html")
def successorderview(request, q=None):
    if not request.user.is_authenticated or not request.user.is_customer:
        return redirect('/')
    mitems=Menu.objects.filter(cart__customer_id=request.user).values('food_name', 'price', 'restaurant_id', 'cart')
    itemlist={}
    prices={}
    for item in mitems:
        if not itemlist.get(item['restaurant_id']):
            itemlist[item['restaurant_id']]={}
        c=Cart.objects.get(pk=item['cart'])
        itemlist[item['restaurant_id']][item['food_name']]=c.quantity
        if not prices.get(item['restaurant_id']):
            prices[item['restaurant_id']]=0
        prices[item['restaurant_id']]+=c.quantity*item['price']
    for item in itemlist:
        res=User.objects.get(restaurant__pk=item)
        js=json.dumps(itemlist[item])
        order=Orders.objects.create(order_id=q, customer_id=request.user, restaurant_id=res, items=js, total_price=int(prices[item]))
        order.save()
    Cart.objects.filter(customer_id=request.user).delete()
    return render(request=request, template_name="successorder.html")
# def orderscompleteview(request, o=None, q=None):
#     if not request.user.is_authenticated or not request.user.is_customer:
#         return redirect('/')
#     cust_id=request.user.pk
#     items=Menu.objects.filter(cart__customer_id=request.user).values('food_name', 'price', 'restaurant_id', 'cart')
#     print(items)
#     restaurants={}
#     for item in items:
#         info['rest']=True
#         if item['restaurant_id'] not in restaurants:
#             restaurants[item['restaurant_id']]={}
#             restaurants[item['restaurant_id']]['items']={}
#             res=Restaurant.objects.get(pk=item['restaurant_id'])
#             restaurants[item['restaurant_id']]['rest_name']=res.res_name
#             restaurants[item['restaurant_id']]['pickuplat']=str(res.latitude)
#             restaurants[item['restaurant_id']]['pickuplong']=str(res.longitude)
#         c=Cart.objects.get(pk=item['cart'])
#         restaurants[item['restaurant_id']]['items'][item['food_name']]={}
#         restaurants[item['restaurant_id']]['items'][item['food_name']]['price']=item['price']*c.quantity
#         restaurants[item['restaurant_id']]['items'][item['food_name']]['quantity']=c.quantity
#     print(restaurants)
#     return render(request=request, template_name="order.html", context={"info": info, "rests": restaurants})
def finishorderview(request, q=None):
    if not request.user.is_authenticated or not request.user.is_delivery:
        return redirect('/')
    print(q)
    Orders.objects.filter(order_id=q).update(exec_id=request.user)
    return render(request=request, template_name="homeDel.html", context={'msg': "Delivery Completed!"})
def logout_request(request):
    logout(request)
    return redirect('/')




