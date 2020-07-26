from django.urls import path
from . import views

app_name = 'post'

# 메뉴 등록 !!

urlpatterns = [
    path("", views.main, name="main1"),
    path("post_list/", views.post_list, name="post_l"),
    #post_list라는 메뉴를 추가한 것
    path("post_list/<int:pk>/", views.post_detail, name="post_d"),
    path("post_create/", views.post_create, name="post_c"),
    # path("post_update/<int:pk>/", views.post_update, name="post_u"),
    # path("post_delete/<int:pk>/", views.post_delete, name="post_del"),

]