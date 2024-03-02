from django.urls import path
from .views import HomePageView
# from .views import home

urlpatterns = [
    path('',HomePageView.as_view(),name='home')
    # path('',home,name='home')
    
]