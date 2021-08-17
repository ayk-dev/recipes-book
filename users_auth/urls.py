from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterUserView, LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

]