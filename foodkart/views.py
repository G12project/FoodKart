from django.shortcuts import  render, redirect
from .forms import NewCustomerForm, NewRestaurantForm, NewDeliveryExecForm
from django.contrib.auth import login, authenticate,  logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .models import User, Menu
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

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
		return redirect('/')
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
				return redirect('/welcome')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="loginCustomer.html", context={"login_form":form})
class Menulist(ListView,LoginRequiredMixin, UserPassesTestMixin):
	model=Menu
	template_name='menu_list.html'
	def get_queryset(self):
        return Menu.objects.filter(restaurant_id=self.request.user)

class AddFood(CreateView, LoginRequiredMixin, UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_restaurant
	model=Menu
	fields = ['food_name','description','food_image','veg','price']
	template_name='updatefood.html'
	def form_valid(self, form):
		form.instance.restaurant_id = self.request.user
		return super().form_valid(form)
	success_url = reverse_lazy('menu_list')

class UpdateFood(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_restaurant
	model=Menu
	fields=['food_name','description','food_image','veg','price']
	template_name='updatefood.html'
	success_url=reverse_lazy('menu_list')
class DeleteFood(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_restaurant
	model=Menu
	template_name='deletefood.html'
	success_url=reverse_lazy('menu_list')

class Home(ListView,LoginRequiredMixin, UserPassesTestMixin):

	model=Menu
	template_name='home.html'

	def test_func(self):
		return self.request.user.is_customer
	
	def get_context_data(self, **kwargs):
        con = super(Home, self).get_context_data(**kwargs)
        con['search']=SearchForm()
        return con

class SearchFood(ListView,LoginRequiredMixin, UserPassesTestMixin):

	model=Menu
	template_name'Search.html'

	def test_func(self):
		return self.request.user.is_customer
	def get_queryset(self):
        food = self.request.GET.get('search','')
        if not Menu.objects.filter(food_name=food).exists():
            return None
        object_list=Menu.objects.filter(food_name=food)
        return object_list

class DetailFood(DetailView,LoginRequiredMixin, UserPassesTestMixin):

	model=Menu
	template_name='Detail.html'
	def test_func(self):
		return self.request.user.is_customer

	












