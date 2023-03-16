from rest_framework import serializers
from . import models
from datetime import date
from rest_framework.validators import UniqueValidator
from . import models


def is_after_today(value):
    if value > date.today():
        raise serializers.ValidationError('Дата регистрации не должна быть раньше текушей даты!')


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=models.User.objects.all())], write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password2 = serializers.CharField(max_length=20, write_only=True)

    registered_date = serializers.DateField(
        validators=[is_after_today, ]
    )

    class Meta:
        model = models.Author
        # fields = '__all__'
        exclude = ['user', ]
        validators = [
            serializers.UniqueTogetherValidator(queryset=models.Author.objects.all(),
                                                fields=['name', 'phone_number'],
                                                message='Unical')
        ]

    def create(self, validated_data):
        user = models.User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        author = models.Author.objects.create(
            name=validated_data['name'],
            birth_date=validated_data['birth_date'],
            registered_date=validated_data['registered_date'],
            phone_number=validated_data['phone_number'],
            user=user
        )
        return author

    def validate_name(self, value):
        if ' ' not in value:
            raise serializers.ValidationError('Введите ФИО полностью!')
        return value

    def validate_phone_number(self, value):
        if '0' not in value[0]:
            raise serializers.ValidationError('Номер должен начинаться с нуля!')
        return value

    def validate(self, data):
        if data['registered_date'].year - data['birth_date'].year < 18:
            raise serializers.ValidationError('Вам должно быть более 18 лет!')

        if data['password'] != data['password2']:
            raise serializers.ValidationError('ldskfj')
        return data




