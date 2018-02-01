from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
    # 1. 브라우저에서 요청 -> runserver
    # 2. 요청이 runserver로 실행중인 서버에 도착
    # 3. runserver는 요청을 Django code로 전달
    # 4. Django code중 config.urls모듈이 해당 요청을 받음
    # 5. config.urls모듈은 ''(admin/를 제외한 모든 요청)을 blog.urls모듈로 전달
    # 6. blog.urls모듈은 받은 요청의 URL과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일차하는 패턴과 연결된 함수(view)를 실행
    #  7-1. settings모듈의 TEMPLATES속성 내의 DIRS목록에서
    #       blog/post_list.html파일의 내용을 가져옴
    #  7-2. 가져온 내용을 적절히 처리(렌더링, render()함수)하여 리턴
    # 8. 함수의 실행 결과(리턴값)를 브라우저로 다시 전달

    # HTTP 프로토콜로 텍스트 데이터 응답을 반환
    # return HttpResponse('Post List')
    # return HttpResponse('<html><body><h1>Post List</h1></body></html>')


    # 생성된 순서대로 출력하고 싶을 때
    posts = Post.objects.order_by('-created_date')


    # posts = Post.objects.all()
    # render()함수에 전달할 dict객체 생성
    context = {
        'posts' : posts,
    }
    return render(   # rander라는 특수한 함수는 전달된 딕셔너리 키 값으로
        request=request,      # template이 쿼리셋을 참조가능함.
        template_name='blog/post_list.html',
        context=context,
    )
    # 'blog/post_list.html'템플릿 파일을 이용해 HTTP프로토콜
    # return render(request, 'blog/post_list.html')
    #               -> 위와 같은 말. 단순히 키워드 인자로 주어준것일 뿐.


def post_detail(request, pk):
    # 디버깅 하는 방법
    # return HttpResponse(pk)

    post = Post.objects.get(pk=pk)

    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


def post_edit(request, pk):

    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('blog:post-detail', pk=pk)

    else:
        context = {
            'post' : post,
        }
        return render(request, 'blog/post_edit.html', context)






# def post_delete(request, pk):
#     post = Post.objects.get(pk=pk)
#     post.delete()
#
#     posts = Post.objects.all()
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/post_list.html', context)


def post_delete(request, pk):

    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user == post.author:
            post = Post.objects.get(pk=pk)
            post.delete()
            return redirect('blog:post-list')
        return redirect('blog:post-detail', pk=pk)

    else:
         # 요청의 method가 GET일 때
        return render(request, 'blog/post_list.html')



def redirect_to_list(request):
    return redirect('blog:post-list')
                    # 네이밍 만을 인자로 받고, url은 쓸 수 없음.



def post_add(request):
    # localhost:8000/add로 접근시
    # 이 뷰가 실행되어서 Post add page라는 문구를 보여주도록 urls작성

    pass
    # return HttpResponse('Post add page')
    if request.method == 'POST':

        # 요청의 method가 POST일 때
        # HttpResponse로 POST요청에 담겨온
        # title과 content를 합친 문자열 데이터를 보여줌
        title = request.POST['title']
        content = request.POST['content']
        # return HttpResponse(f'{title} , {content}')

        # ORM을 사용해서 title과 content에 해당하는 Post 생성
        post = Post.objects.create(
            author=request.user,
            title=title,
            content=content,
        )

        # return HttpResponse(f'{post.pk} {post.title} {post.content}')


        # post-detail이라는 URL name을 가진 뷰로
        # 리디렉션 요청을 보냄
        # 이때,  post-detail URL name으로 특정 URL을 만드려면
        # pk값이 필요하므로 키워드 인수로 해당 값을 넘겨준다.
        return redirect('blog:post-detail', pk=post.pk)
                        # 이것 자체가 주소.
    else:
        # 요청의 method가 GET일 때
        return render(request, 'blog/post_add.html')

# 1. post_add페이지를 보여줌 (GET)
# 2. post_add페이지에서 글 작성 (POST요청)
# 3. post_add view에서 POST요청에 대한 처리 완료후,
#    브라우저에는 post-detail(pk=...)에 해당하는 주소로
#    redirect를 하도록 응답 (301 redirect, URL: /3)
# 4. 브라우저는 301 redirect코드를 갖는 HTTP response를 받고,
#    해당 URL로 GET 요청을 보냄
#    (새로만든 Post의 pk가 3일때) 브라우저는 '/3'주소로 GET요청
# 5. '/3'주소로 온 요청은 다시 runserver -> Django코드
#    -> urls.py -> blog/urls.py
#    -> def post_detail(request, pk)로 도착,
#       post_detail뷰 처리가 완료된 post_detail.html의 내용을 응답
#    -> 브라우저는 해당 내용을 보여줌
