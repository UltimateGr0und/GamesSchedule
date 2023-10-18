from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug:cat_slug>/', CategoryView.as_view(), name='category'),
    path('event/<slug:event_slug>/', EventView.as_view(), name='event'),
    path('addevent/', CreateEvent.as_view(), name='addevent'),
    path('feedback', SendFeedback.as_view(), name='feedback'),
    path('blocked/', temp, name='blocked')
]