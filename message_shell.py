from posts.models import Message
from posts.serializers import MessageSerializer

# message = Message.objects.all().first()

# serializer = MessageSerializer(instance=message)
#
# print(serializer.data)

# create new_message
# new_message_dict = {
#     'text': 'Text for message',
#     'author': 101,
#     'chat': 333
# }


# serializer = MessageSerializer(data=new_message_dict)

# if serializer.is_valid():
#     serializer.save()
# else:
#     print(serializer.errors)


# update message (instance)

# message = Message.objects.all().first()
#
# updated_date = dict(text="Updated text", author=2, chat=301)
#
# serializer = MessageSerializer(instance=message, data=updated_date)
#
# if serializer.is_valid():
#     serializer.save()
# else:
#     print(serializer.errors)



# message = Message.objects.all().first()
#
# serializer = MessageSerializer(instance=message)
#
# print(serializer.data)




# Get message list
#
# messages = Message.objects.all()
#
# serializer = MessageSerializer(instance=messages, many=True)
#
# print(serializer.data)




# create new message without author

new_message_dict = {
    'text': 'Text for message',
    'chat': 333
}


serializer = MessageSerializer(data=new_message_dict)

if serializer.is_valid():
    serializer.save(author=2)
else:
    print(serializer.errors)





