from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from handmade.accounts.views import CreateProfileView, LoginProfileView, EditProfileView, DeleteProfileView, \
    DetailsProfileView

urlpatterns = (
    path('create/', CreateProfileView.as_view(), name='profile create'),
    path('login/', LoginProfileView.as_view(), name='login'),
    path('edit/<int:pk>/', EditProfileView.as_view(), name='profile edit'),
    path('delete/<int:pk>/', DeleteProfileView.as_view(), name='profile delete'),
    path('details/<int:pk>/', DetailsProfileView.as_view(), name='profile details'),
    path('logout/<int:pk>', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logaut'),
)
