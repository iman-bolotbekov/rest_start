"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from posts import views
from accounts import views as acc_views
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

router = routers.DefaultRouter()
router.register('tweet', views.TweetViewSet)
router.register('message', views.MessageViewSet)
router.register('message_frank', views.MyMessageFrankensteinViewSet)

acc_router = routers.DefaultRouter()
acc_router.register('register', acc_views.AuthorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/accounts/', include(acc_router.urls)),
    path('api/token/', auth_views.obtain_auth_token),

    path('api/tweet/', views.create_tweet),
    path('api/message/', views.create_message),
    path('api/message/<int:pk>/', views.detail_message),

    path('api/v-1.0/tweet/', views.TweetCreateListView.as_view()),
    path('api/v-1.0/tweet/<int:pk>/', views.TweetRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v-1.0/message/', views.MessageListCreateAPIView.as_view()),
    path('api/v-1.0/message/<int:pk>/', views.MessageRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v-1.1/', include(router.urls)),

    path('api/v-1.2/message/', views.MyMessageFrankensteinViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v-1.2/message/<int:pk>/', views.MyMessageFrankensteinViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
