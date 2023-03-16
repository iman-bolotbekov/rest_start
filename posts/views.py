import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import views
from rest_framework import authentication
from rest_framework import permissions

from . import models
from . import serializers
from . import my_generics
from .permissions import IsAuthorPermission


@csrf_exempt
def create_tweet(request):
    if request.method == 'GET':
        tweets = models.Tweet.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'title': tweet.title,
                    'body': tweet.body,
                    'author': tweet.author
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = models.Tweet.objects.create(**data)
        json_data = {
            "title": new_tweet.title,
            "body": new_tweet.body,
            "author": new_tweet.author
        }
        return JsonResponse(json_data, safe=False)


class TweetCreateListView(generics.ListCreateAPIView):
    queryset = models.Tweet.objects.all()
    serializer_class = serializers.TweetSerialize

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class TweetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tweet.objects.all()
    serializer_class = serializers.TweetSerialize


class TweetViewSet(viewsets.ModelViewSet):
    queryset = models.Tweet.objects.all()
    serializer_class = serializers.TweetSerialize
    # authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication, ]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorPermission, ]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user.author)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    # authentication_classes = [authentication.BasicAuthentication,
    #                           authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated, ]
    #
    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user.id)


@api_view(['POST', 'GET'])
def create_message(request):
    if request.method == 'POST':
        serializer = serializers.MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        messages = models.Message.objects.all()
        serializer = serializers.MessageSerializer(instance=messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_message(request, pk):
    message = generics.get_object_or_404(models.Message, pk=pk)
    if request.method == 'GET':
        serializer = serializers.MessageSerializer(instance=message)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = serializers.MessageSerializer(instance=message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class MessageListCreateAPIView(my_generics.MyListCreateAPIView):
#     serializer_class = serializers.MessageSerializer
#     model = models.Message

class MessageListCreateAPIView(my_generics.ListMixinAPI, my_generics.CreateMixinAPI, my_generics.MyAPIView):
    serializer_class = serializers.MessageSerializer
    model = models.Message

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MessageRetrieveUpdateDestroyAPIView(my_generics.RetrieveMixinAPI, my_generics.UpdateMixinAPI, my_generics.DeleteMixinAPI, my_generics.MyAPIView):
    serializer_class = serializers.MessageSerializer
    model = models.Message

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# class MyListCreateAPIView(views.APIView):
#     serializer_class = None
#     model = None
#
#     def get_queryset(self):
#         return self.model.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         serializer = self.serializer_class(instance=self.get_queryset(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MessageRetrieveUpdateDestroyAPIView(views.APIView):
#
#     def get_object(self, pk):
#         return generics.get_object_or_404(models.Message, pk=pk)
#
#     def get(self, request, *args, **kwargs):
#         message = self.get_object(kwargs['pk'])
#         serializer = serializers.MessageSerializer(instance=message)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         message = self.get_object(kwargs['pk'])
#         serializer = serializers.MessageSerializer(instance=message, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, *args, **kwargs):
#         message = self.get_object(kwargs['pk'])
#         message.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class MyMessageFrankensteinViewSet(my_generics.ListMixinAPI,
                                   my_generics.CreateMixinAPI,
                                   my_generics.RetrieveMixinAPI,
                                   my_generics.UpdateMixinAPI,
                                   my_generics.DeleteMixinAPI,
                                   viewsets.ViewSet,
                                   my_generics.MyAPIView):
    serializer_class = serializers.MessageSerializer
    model = models.Message
    queryset = models.Message.objects.all()











