from rest_framework import serializers
class HelloSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    gender=serializers.ChoiceField(choices=(('Male','Male'),('Female','Female')))