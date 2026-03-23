from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView , ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin
from rest_framework import viewsets
from django.shortcuts import   get_object_or_404  
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
           

# CURD Operations using Minix Concepts


class GCStudentAPI(GenericAPIView , ListModelMixin ,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self , request , *args , **kwargs):
        return self.list( request , *args , **kwargs)

    def post(self , request , *args , **kwargs):
        return self.create( request , *args , **kwargs)

 
class UPDStudentAPI(GenericAPIView  ,  UpdateModelMixin ,  DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def update(self , request , *args , **kwargs):
        return self.update( request , *args , **kwargs)

    def update(self , request , *args , **kwargs):
        return self.partail_update( request , *args , **kwargs)    

    def delete(self , request , *args , **kwargs):
        return self.destroy( request , *args , **kwargs)

#  CURD with the Concrete  View Classes



class LCStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer        



# CURD with Viewsets 


class StudentAPIView(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        stu = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def update(self, request, pk=None):
        stu = get_object_or_404(Student, pk=pk)        
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        stu = get_object_or_404(Student, pk=pk)
        stu.delete()
        return Response({'msg': 'Deleted Data'}, status=status.HTTP_204_NO_CONTENT) 

 
 
#CURD with ModelViewSets
# 

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

# Read only 
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
