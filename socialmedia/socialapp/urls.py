from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('show/',views.show,name='show'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('post/',views.post,name='post'),
    path('allpic/',views.allpic,name='allpic'),
    path('like/',views.like,name='like')
]
