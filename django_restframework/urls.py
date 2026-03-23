
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.welcome),
    # path('studentapi/' , views.student_api), 
    # path('studentapi/<int:pk>/' , views.student_api)

    path('studentapi/' , views.LCStudent.as_view()), 
    path('studentapi/<int:pk>/' , views.UPDStudentAPI.as_view())

]
