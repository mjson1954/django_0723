from django.db import models
# 모델은 db(식자재)를 담는 용기

class Post(models.Model): # 게시판의 글을 담는 모델
    title = models.CharField(max_length=255, null=True) 
    # null=True: 아무것도 적지 않는 것을 허용하겠다
    content = models.TextField(null=True)
    # TextField는 max length가 정해져있지 않은 문자열을 저장할 때 사용
    writer = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 모델 객체가 만들어지는 순간(created_at), 마지막 수정 시간을 저장(updated_at)
    # 게시판의 글은 위 다섯개의 요소로 구성된다.
