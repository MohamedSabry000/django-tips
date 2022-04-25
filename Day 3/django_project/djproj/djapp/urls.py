from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/<st_id>', views.show, name='show'),
    path('del/<st_id>', views.del_St, name='del'),
    path('add/', views.addStudent, name='add'),
    path('edit/<st_id>', views.editStudent, name='edit'),
    
    # rest_framework path
    path('api-all/', views.api_all_students, name='api-all'),
    path('api-one/<st_id>', views.api_one_student, name='api-one'),
    path('api-add/', views.api_add_student, name='api-add'),
    path('api-edit/<st_id>', views.api_edit_student, name='api-edit'),
    path('api-del/<st_id>', views.api_del_student, name='api-del'),


# {
#         "fname": "wael",
#         "lname": "NoName",
#         "age": 2,
#         "student_track": 1
# }
]
