from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer




def welcome():
    return Respose('Welcome to Django')

# Create your views here.
@api_view(['GET' ,'POST' , 'PUT' , 'DELETE' ])
def StudentAPI(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu =  Student.objects.get(id=id)
            seriliazer = StudentSerializer(stu)
            return Response(seriliazer.data)

    stu = Student.objects.all()
    serializer = StudentSerializer(stu , many=True)
    return Response(serializer.data)        
