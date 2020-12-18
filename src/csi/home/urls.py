from django.urls import path
from. import views

urlpatterns=[
    path('',views.index,name="home"),
    # path('/about',views.contact,name="home-about"),
    # path('/contact',views.contact,name="home-contact"),
    path('event/',views.events,name="home-event"),
]