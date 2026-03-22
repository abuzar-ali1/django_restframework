from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin


def welcome(request):
    return HttpResponse('<h1>Welcome in the Django</h1>')

# # Create your views here.



# @api_view(['GET' ,'POST' , 'PUT' ,  'PATCH', 'DELETE' ])
# def student_api(request , pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu =  Student.objects.get(id=id)
#             seriliazer = StudentSerializer(stu)
#             return Response(seriliazer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu , many=True)
#         return Response(serializer.data , status=status.HTTP_201_CREATED)     

#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data Posted'})
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)     

#     elif request.method == 'PUT':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu , data=request.data )
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data' : 'Data Successfully Updated'})
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)     

#     elif request.method == 'PATCH':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu , data=request.data , partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data' : 'Data Successfully Updated'})
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST) 

#     elif request.method == 'DELETE':
#         id =  pk
#         stu =  Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'res' : 'Data Deleted'})


# Same View using the APIView

class StudentAPI(APIView):
    def get(self , request ,  pk = None , format=None):
        id = pk
        if id is not None:
            stu =  Student.objects.get(id=id)
            seriliazer = StudentSerializer(stu)
            return Response(seriliazer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

    def post(self , request , format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Posted'})
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)   

    def put(self , request , pk ,  format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu , data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : 'Data Successfully Updated'})
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)     

    def patch(self , request,  pk , format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu , data=request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : 'Data Successfully Updated'})
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST) 
    def delete(self , request , pk , format=None):
        id =  pk
        stu =  Student.objects.get(pk=id)
        stu.delete()
        return Response({'res' : 'Data Deleted'})
           


class StudentList(GenericAPIView , ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self , request , *args , **kwargs):
        return self.list( request , *args , **kwargs)


class StudentCreate(GenericAPIView , CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self , request , *args , **kwargs):
        return self.create( request , *args , **kwargs)

 