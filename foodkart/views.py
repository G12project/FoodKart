from django.shortcuts import  render, redirect
from .forms import NewCustomerForm, NewRestaurantForm, NewDeliveryExecForm
from django.contrib.auth import login, authenticate,  logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .models import User

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