from django.urls import path, include
from . import views
from customer import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index, name = 'index'),
    path('about/',views.about, name = 'about'),
    path('order/',views.order, name = 'order'),
    path('post/',views.post, name = 'post'),



]