from django.urls import path
from . import views


urlpatterns = [
    path('getCellCerti/', views.getCellCerti, name='getCellCerti'),
    path('signup/', views.signUp, name="signup"),
    path('signin/', views.signIn, name="signin"),
    path('getUserId/', views.getUserId, name='getUserId'),
]
