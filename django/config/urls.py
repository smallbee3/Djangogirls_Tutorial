"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls), # 'admin/' 로 오는모든 것들을 admin.site.urls로 매치
    # path('', include('blog.urls')), # '' 아무것도 없을때 (root url일때)
                                    # 이거에 대한 url패턴이 일치하는지
                                    # 블로그라는 패키지안에있는 urls 라는
                                    # 모듈을 참조하겠다..
    # '' : admin외에는 모두 'blog.urls'로 보낸다는 의미.
    path('', include(('blog.urls', 'blog'), namespace='blog'))  # '' 아무것도 없을때 (root url일때)

    # path('', include('blog.urls')),  # '' 아무것도 없을때 (root url일때)

]
