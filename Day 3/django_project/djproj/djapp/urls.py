from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/<st_id>', views.show, name='show'),
    path('del/<st_id>', views.del_St, name='del'),
    path('add/', views.addStudent, name='add'),
    path('edit/<st_id>', views.editStudent, name='edit'),
    
]
