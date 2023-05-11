from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='sign_up_view'), # /users/signup/
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login_view'), # /users/login/
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"), # /users/refresh/
    
    path('profile/<int:user_id>/', views.ProfileView.as_view(), name="profile_view"), # /users/profile/<int:user_id>/
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='follow_view'), # /users/follow/<int:user_id>/
    path("withdraw/<int:user_id>/", views.ProfileView.as_view(), name="token_refresh"), # /users/withdraw/

    path("auth/password/reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("auth/password/reset/b'<str:uidb64>'/<str:token>/", views.PasswordTokenCheckView.as_view(), name="password_reset_confirm"),
    path("auth/password/reset/confirm/", views.SetNewPasswordView.as_view(), name="password_reset_confirm"),

    path("verify-email/b'<str:uidb64>'/<str:token>/", views.VerifyEmailView.as_view(), name='verify-email'),
    
]
