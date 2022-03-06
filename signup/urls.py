from django.urls import path 
from . import views 
app_name='signup'
urlpatterns=[
 
  path("",views.home,name="home"),
  path('registerpage/',views.registerpage,name="registerpage"),
  path('login/',views.loginpage,name="login"),
  path('logout/' ,views.logoutpage,name='logout'),
    
]