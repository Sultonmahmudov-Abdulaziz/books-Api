from rest_framework import serializers

class BooksSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField()

