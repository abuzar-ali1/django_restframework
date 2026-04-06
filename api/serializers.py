from rest_framework import serializers
from .models import Student , Song , Singer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name' , 'roll' , 'city']
        
class SongSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Song
        fields = ['id', 'title' , 'singer']
        
class SingerSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many=True)
    songby = SongSerializer(many=True, read_only=True, source='song')

    class Meta:
        model = Singer
        fields = ['id', 'name' , 'gender' , 'song' , 'songby']
        

