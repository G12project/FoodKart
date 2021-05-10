from django.urls import path
from . import views
from django.conf.urls import url

app_name = "main"


urlpatterns = [
	path('register/', views.CustomerRegisterView.as_view(), name="register"),
	path('', views.loginview, name="login"),
	path('registerres/', views.RestaurantRegisterView.as_view(), name="resregister"),
	path('registerdel/', views.DeliveryExecRegisterView.as_view(), name="delregister"),
	path('view', views.Menulist.as_view(), name='menu_list'),
	path('add', views.AddFood.as_view(), name='addfood'),
	path('update/<int:pk>', views.UpdateFood.as_view(), name='updatefood'),
	path('delete/<int:pk>', views.DeleteFood.as_view(), name='deletefood'),
	path('detail/<int:pk>', views.DetailFood.as_view(), name='Detail'),
	path('home', views.Home.as_view(), name='home'),
	path('search', views.SearchFood.as_view(), name='Search'),
	

	

	# path('logout/', views.logoutview, name="logout"),
	# path('welcome/', views.Dashboardview.as_view(), name="welcome"),
	# path('article/', views.CreateArticleview.as_view(), name="article"),
	# path('search/', views.SearchResview.as_view(), name="searchresults"),
]