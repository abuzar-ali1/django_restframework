from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer




def welcome():
    return Respose('Welcome to Django')

# Create your views here.
@api_view(['GET' ,'POST' , 'PUT' ,  'PATCH', 'DELETE' ])
def student_api(request , pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu =  Student.objects.get(id=id)
            seriliazer = StudentSerializer(stu)
            return Response(seriliazer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data , , status=status.HTTP_201_CREATED)     

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Posted'})
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)     

    elif request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu , data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : 'Data Successfully Updated'})
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)     

    elif request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu , data=request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : 'Data Successfully Updated'})
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        id =  pk
        stu =  Student.objects.get(pk=id)
        stu.delete()
        return Response({'res' : 'Data Deleted'})