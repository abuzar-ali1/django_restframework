from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.reponse import Response
from .models import Student
from .serializers import StudentSerializers



# Create your views here.
@api_view(['GET' ,'POST' , 'PUT' , 'DELETE' ])

def StudentAPI(request):
    if request.method == 'GET':
        id = request.data.get(id)
        if id is not None:
            stu =  Student.objects.get(id=id)
            seriliazer = StundetSerializer(stu)
            return Response(serializer.data)

    stu = Student.objects.all()
    serializer = StundetSerializer(Stu)
    return Reponse(serializer.data)        
