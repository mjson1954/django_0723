from django.shortcuts import render, redirect
from django.urls import reverse
# from .models import Post
from . import models

def main(request):
    return render(request, "post/main.html")

def post_list(request):
    all_posts = models.Post.objects.all() # db에 있는 Post 객체들을 전부 가져와라.
    # all posts는 Post모델로 만들어진 Post객체가 리스트로 담긴다.
    ctx = {
        "posts": all_posts # 나중에 template에서 사용할 context들을 저장하는 딕셔너리.
        # post_list.html에서 posts로 post 객체들 가져옴. 
    }
    return render(request, "post/post_list.html", ctx)

def post_detail(request, pk):
    post1 = models.Post.objects.get(pk=pk) # pk가 pk인 객체만 가져오겠다.
    ctx = {
        "post": post1 # post중에서 Post1만 담아주겠다.
    }
    return render(request, "post/post_detail.html", ctx)


def post_create(request):
    if request.method == "POST":
        # 새로운 객체를 만든다 (create)
        new_Post = models.Post.objects.create( 
            title = request.POST.get("tit"), 
            # post_create.html에서 name에 해당하는 애들을 사용해서 가져오는 방법
            writer = request.POST.get("wri"),
            content = request.POST.get("con"),
        )
        new_pk = new_Post.pk # 새로운 객체의 pk

        address = 'post/post_list/'+str(new_pk)+'/' # 절대경로
        # reutrn redirect(address) # 절대 경로로도 보낼 수 있음.

        return redirect(reverse('post:post_d', kwargs={'pk': new_pk}))
        # 새로운 객체를 만들자마자 post_detail.html을 통해 만든 내용을 보여줌.
        
    else:
        return render(request, "post/post_create.html") # get 요청 처리

# def post_update():

# def post_delete():
