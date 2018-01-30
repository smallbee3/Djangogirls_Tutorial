import re
from django.urls import path, re_path
from . import views
# .은 얘가 속하는 현재 위치
# from blog import views랑 같은 말.
# from은 소스루트를 기준으로할 때 blog라는 패키지를 할 때 .
# 절대경로를 권장하지 않음.

urlpatterns = [
    path('list', views.post_list, name='post-list'),

    # 3/
    # 53/
    # 53/asdf/ <- X
    # path('detail/', views.post_detail),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    # 만약 post/라고 바꾸고 싶으면 일일이 다 바꿔야함.

    # 숫자가 1개 이상 반복되는 경우를 정규표현으로 구현하되
    # 해당 반복구간을 그룹으로 묶고, 그룹 이름을 'pk'로 지정
    # re.compile(r'(?P<pk>\d+)')
    # path()
]