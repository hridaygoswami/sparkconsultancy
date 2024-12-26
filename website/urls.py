from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='Index'),
    path("contact", views.contact, name='Contact'),
    path("properties", views.properties, name='Properties'),
    path("properties/single", views.propertiesSingle, name='Properties Single'),
    path("about", views.about, name='About'),
    path("services", views.services, name='Services'),
    path("blog", views.blog, name='Blog'),
    path("blog/single", views.blogSingle, name='Blog Single')
]