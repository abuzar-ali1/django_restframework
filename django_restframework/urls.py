
from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# router.register('studentapi' , views.StudentAPIView , basename='Stundent')
# router.register('studentapi' , views.StudentModelViewSet , basename='Stundent')
router.register('studentapi' , views.StudentModelViewSet , basename='Stundent')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.welcome),
    # path('studentapi/' , views.student_api), 
    # path('studentapi/<int:pk>/' , views.student_api)
    path('api/' , include(router.urls)),
    path('auth/' , include('rest_framework.urls')),
    # path('studentapi/' , views.LCStudent.as_view()), 
    # path('studentapi/<int:pk>/' , views.RUDStudent.as_view())

]
