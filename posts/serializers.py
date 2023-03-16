from rest_framework import serializers
from . import models


class TweetSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Tweet
        fields = '__all__'
        # exclude =['author', ]
        read_only_fields = ['author', ]


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(required=False)
    chat = serializers.IntegerField()
    user_id = serializers.IntegerField(read_only=True)

    def save(self, **kwargs):
        print('Create new message!')
        return super().save(**kwargs)

    def create(self, validated_data):
        message = models.Message.objects.create(
            text=validated_data['text'],
            chat=validated_data['chat'],
            user_id=validated_data['user_id']
        )
        return message

    def update(self, instance, validated_data):
        text = validated_data.get('text')
        chat = validated_data.get('chat')
        if text:
            instance.text = text
        if chat:
            instance.chat = chat
        instance.save()
        return instance

