import re
from django.urls import path, re_path

from blog.views import redirect_to_list
from . import views
# .은 얘가 속하는 현재 위치           -> 상대경로 import
# from blog import views랑 같은 말 -> 절대경로 import
# from은 소스루트를 기준으로할 때 blog라는 패키지가 있기때문에 from blog를 불러올 수 있음.
# 절대경로를 권장하지 않음.


                # 1) views를 통째로 import 했기 때문에
urlpatterns = [
    path('', views.post_list, name='post-list'),
                 # 2) 함수를 호출하는게 아니라 함수 자체를 전달.
                 # 3) 나중에 이 함수가 필요할 때 실행시킬 수 있음.

    # 3/
    # 53/
    # 53/asdf/ <- X
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),

    # path('detail/', views.post_detail),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    # 만약 post/라고 바꾸고 싶으면 일일이 다 바꿔야함.

    # 숫자가 1개 이상 반복되는 경우를 정규표현으로 구현하되
    # 해당 반복구간을 그룹으로 묶고, 그룹 이름을 'pk'로 지정
    # re.compile(r'(?P<pk>\d+)')
    # path()



    path('add/', views.post_add, name='post-add'),



    # /3/delete/
    path('<int:pk>/delete/', views.post_delete, name='post-delete'),

    path('', redirect_to_list, name='home'),

]

