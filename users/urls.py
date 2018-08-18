# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('download/', views.download, name='download'),
    path('add-asset/', views.add_asset, name="add_asset"),
    path('get-all-user-asset/', views.get_all_user_asset, name="get-all-user-asset"),
]