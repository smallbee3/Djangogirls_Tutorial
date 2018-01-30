import re
from django.urls import path, re_path
from . import views
# .은 얘가 속하는 현재 위치
# from blog import views랑 같은 말.
# from은 소스루트를 기준으로할 때 blog라는 패키지를 할 때 .
# 절대경로를 권장하지 않음.

urlpatterns = [
    path('', views.post_list),

    # 3/
    # 53/
    #
    # path('detail/', views.post_detail),
    re_path(r'(?P<pk>\d+)/$', views.post_detail),


    # 숫자가 1개 이상 반복되는 경우를 정규표현으로 구현하되
    # 해당 반복구간을 그룹으로 묶고, 그룹 이름을 'pk'로 지정
    # re.compile(r'(?P<pk>\d+)')
    # path()
]