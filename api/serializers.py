from rest_framework import serializers



class BooksSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=5000)
    image = serializers.ImageField()


