from django.urls import path
from .import views

urlpatterns = [
    path('create_post/',views.Post_Create_View.as_view(), name='create_post'),
    path('post_update/<int:pk>/', views.Post_Update_View.as_view(), name='update_post'),
    path('post_delete/<int:pk>/', views.Post_Delete_View.as_view(), name='delete_post'),
    path('post_list/', views.Post_List_View.as_view(), name='post_list'),
    path('post_detail/<int:pk>/', views.Post_Detail_View.as_view(), name='post_detail'),
    path('post_like/<int:pk>', views.Post_Like_View.as_view(), name='post_like'),
]