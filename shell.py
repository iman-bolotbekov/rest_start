import io
# from django.utils import timezone
from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(
    email = 'some_email@gmail.kg',
    content='Some text about smth'
)

# print(comment.email)
# print(comment.content)


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


serializer = CommentSerializer(comment)
print(serializer.data)

json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = io.BytesIO(json_data)

data = JSONParser().parse(stream)

serializer = CommentSerializer(data=data)
# print(serializer)
serializer.is_valid()
print(serializer.validated_data)




