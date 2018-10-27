from django.urls import path
from .views import HomePageView, AboutYouView

urlpatterns = [
  path('about/', AboutYouView.as_view(), name='about'),
  path('', HomePageView.as_view(), name='home')
]
