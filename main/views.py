from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
# View에 Model(Post) 가져오는거
from .models import Post
from .forms import PostForm

#index.html 불러오기
def index(request):
    return render(request,'main/community.html')

#community.html 불러오기
def community(request):
    #모든 post 불러오게 했삼
    postlist = Post.objects.all()
    #postlist 불러오게 뒤에 추가했삼
    return render(request,'main/community.html', {'postlist':postlist})

#community 게시글 가져올 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    postlist = Post.objects.all()
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post, 'postlist':postlist})


def newpost(request):
    if request.method == 'POST':
        # request.FILES사용해야 사진 업로드가 됨
        mainphoto = request.FILES.get('mainphoto')
        if mainphoto:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                username=request.POST['username'],
                contents=request.POST['contents'],
                mainphoto=mainphoto,  # 사진 위에거 얻어온거 지정함
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                username=request.POST['username'],
                contents=request.POST['contents'],
            )
        return redirect('/community/')
    return render(request, 'main/newpost.html')

class PostCreateView(CreateView):
    template_name = 'main/newpost.html'
    success_url = '/community/'
    form_class = PostForm