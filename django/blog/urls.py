from django.urls import path
from . import views
# .은 얘가 속하는 현재 위치
# from blog import views랑 같은 말.
# from은 소스루트를 기준으로할 때 blog라는 패키지를 할 때 .
# 절대경로를 권장하지 않음.

urlpatterns = [
    path('', views.post_list),
    path('detail/', views.post_detail),
]