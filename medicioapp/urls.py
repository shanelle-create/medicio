
from django.contrib import admin
from django.urls import path
from medicioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('inner/', views.inner,name='inner'),
    path('about/', views.about,name='about'),
    path('doctors/', views.doctors,name='doctors'),
    path('departments/', views.departments,name='departments'),
    path('contact/', views.contact,name='contact'),

]
