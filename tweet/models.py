# tweet/models.py
from django.db import models
from user.models import (
    UserModel,
)  # user앱에 있는 모델을 가져와서 사용할건데 그 모델 중 이름이 UserModel인 친구를 가져오겠다.!
from taggit.managers import TaggableManager


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    author = models.ForeignKey(
        UserModel, on_delete=models.CASCADE
    )  # foreignkey는 다른 데이터베이스(UserModel)에서 내용을 가져오겠다! 라는 의미
    content = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TweetComment(models.Model):
    class Meta:
        db_table = "comment"

    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
