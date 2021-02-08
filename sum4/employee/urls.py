from django.urls import path
from.import views
urlpatterns = [
    path('',views.profile),
    path('profile/',views.profile,name='employee,profile'),


]
