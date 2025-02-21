from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
urlpatterns = [
    path('Sign_Up', views.User_Profile_View.as_view(), name='Sign_Up'),
    path('Login/', views.CustomLoginView.as_view(template_name='Login_Form.html'), name='Login'),
    path('Logout/',LogoutView.as_view(next_page='Login'), name='Logout'),
    path('user_profile/', views.User_Profile_Details_View.as_view(), name='User_Profile'),
    path('edit_user_profile/', views.User_Profile_Edit_View.as_view(), name='edit_profile'),
    path('change_password/', PasswordChangeView.as_view(template_name = 'password_change_form.html'), name='password_change'),
    path('change_password_done/',PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done')
]