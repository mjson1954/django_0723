from django.contrib import admin
from .models import Post

admin.site.register(Post) # 만든 model인 post를 admin.py에 등록해준 것
# 등록을 안하면 admin 사이트에서 Post 부분이 아예 뜨지 않음