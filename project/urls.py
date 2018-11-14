"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contact_box import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.new_person, name="new_person"),
    path('modify/<int:id>/', views.modify_person, name="modify_person"),
    path('delete/<int:id>/', views.delete_person, name="delete_person"),
    path('show/<int:id>/', views.show_person, name="show_person"),
    path('homepage', views.all_people, name="all_people"),
    path('address', views.all_address, name="all_address"),
    path('add_address', views.add_address, name="add_address"),
    path('select_address/<int:id>', views.select_address, name="select_address"),
    path('edit_address/<int:id>/', views.edit_address, name="edit_address"),
    path('delete_address/<int:id>/', views.delete_address, name="delete_address"),
    path('add_email/<int:id>', views.add_email, name="add_email"),
    path('add_phone/<int:id>', views.add_phone, name="add_phone"),
    path('delete_email/<int:id>/', views.delete_email, name="delete_email"),
    path('delete_phone/<int:id>/', views.delete_phone, name="delete_phone"),
    path('delete_person_address/<int:id>/', views.delete_person_address, name="delete_person_address"),
    path('group_add/', views.group_add, name="group_add"),
    path('groups/', views.all_groups, name="all_groups"),
    path('edit_group/<int:id>/', views.edit_group, name="edit_group"),
    path('delete_group/<int:id>/', views.delete_group, name="delete_group"),
    path('group_detail/<int:id>/', views.group_detail, name="group_detail"),
    path('person_group/<int:id>/', views.person_group, name="person_group"),
    path('groupSearch/', views.group_search, name="group_search"),
]
