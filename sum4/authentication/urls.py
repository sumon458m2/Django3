from django.urls import path
from.import views
urlpatterns = [
    path('',views.authentication),
    path('forgot_password/',views.forgot_password),
    path('registration/',views.registration),
    path('logout/',views.userlogout),

]
