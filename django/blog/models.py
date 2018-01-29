from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    content_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    # https://nachwon.github.io/django-6-admin/
    # 이제 다시 관리자 페이지를 확인해보면 글 제목이 목록에 보이는 것을 확인할 수 있다.
    def __str__(self):
        return self.title