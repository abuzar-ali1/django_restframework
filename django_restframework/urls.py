
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.welcome),
    # path('studentapi/' , views.student_api), 
    # path('studentapi/<int:pk>/' , views.student_api)

    # path('studentapi/' , views.StudentRetrieve.as_view()), 
    path('studentapi/<int:pk>/' , views.StudentRetrieve.as_view())

]
