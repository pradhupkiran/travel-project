from django.urls import path
from . import views

urlpatterns = [

    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('detail/',views.detail),
    path('thanks/',views.thanks),
    path('result/',views.opreartion)
]