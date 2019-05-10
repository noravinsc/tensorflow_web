"""tensorflow_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from word2vec import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('word2vec/', views.word2vec),

    path('websocket', views.WebSocket, name="WebSocket"),
    path('word2vec_api', views.word2vec_api, name="word2vec_api"),

    path('test_popen', views.test_popen, name="test_popen"),
    path('test_out', views.test_out, name="test_out"),
]
