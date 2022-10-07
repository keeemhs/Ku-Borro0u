# from ssl import _PasswordType
from django.shortcuts import render, redirect
# from .models import Building, Employee, Visitor
from .models import User, Article, AuthUser
from django.views.generic.base import TemplateView
from django.contrib import auth, messages
from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from proj.settings import SECRET_KEY
from django.http  import JsonResponse,HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q

class MainpageView(TemplateView):
    template_name = 'app/main.html'

def main_view(request):
   return render(request, 'main.html')

def bui_view(request):
    users = User.objects.all()
    return render(request, 'app/bui.html', {"users":users})

##########################################

def borrow(request):
   if not request.user.is_authenticated:
      return redirect('login')
   articles = Article.objects.all()
   return render(request, 'app/borrow.html', {"articles":articles})
   

def bui(request):
   return render(request, 'app/bui.html')

def contact(request):
   return render(request, 'app/contact.html')    

def detail(request):
   if not request.user.is_authenticated:
      return redirect('login')
   articles = Article.objects.all()
   return render(request, 'app/detail.html', {"articles":articles})

def find_id_pwd(request):
   if not request.user.is_authenticated:
      return redirect('login')
   return render(request, 'app/find_id_pwd.html')

# def login(request):
#    return render(request, 'app/login.html')


def passwdreset(request):
   return render(request, 'app/passwdreset.html')

# def regist(request):
#    return render(request, 'app/regist.html')

def rented_other_detail(request):
   return render(request, 'app/rented_other_detail.html')


def search_result(request):
   return render(request, 'app/search_result.html')

@csrf_exempt
def sign_up(request):
   if request.method == 'POST':
      user = AuthUser()
      user.email = request.POST['email']
      user.password = make_password(request.POST['password'])
      user.phone = request.POST['phone']
      # user.borrow_code = request.POST['borrow_code']
      # user.regist_code = request.POST['regist_code']
      user.major = request.POST['major']
      user.undergrad = request.POST['undergrad']
      # user.nickname = request.POST['nickname']
      user.username = request.POST['username']
      user.name = request.POST['name']
      user.is_superuser = '0'
      user.is_staff = '0'
      user.is_active = '0'
      user.save()
      return redirect('main')
   else:
      user = User.objects.all()
      return render(request,'app/sign_up.html', {'user':user})


def sign_in(request):
   return render(request, 'app/sign_in.html')

def wish_detail(request):
   return render(request, 'app/wish_detail.html')



def bui_view(request):
    users = User.objects.all()
    articles = Article.objects.all()
    return render(request, 'app/bui.html', {"users":users, "articles":articles})

def article_view(request):
    articles = Article.objects.all()
    return render(request, 'app/borrow.html', {"articles":articles})

def login_check(request):
   users = User.objects.all()
   return render(request, "app/mypage.html", {"users":users})

def login(request):
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      # user = auth.authenticate(request, username=username, password=password)
      user = authenticate(username=username, password=password)
      if user is not None: #로그인 정보가 있다면
         # auth.login(request, user)
         auth_login(request, user)
         return redirect('main')
      else: #로그인 정보가 없다면
         auth_logout(request)
         return render(request, 'app/login.html', {'error': 'username or password is incorrect'})
   else:
      auth_logout(request)
      return render(request, 'app/login.html')

def mypage(request):
   if not request.user.is_authenticated:
      return redirect('login')
   
   return render(request, 'app/mypage.html')



def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('bui')
    return render(request,'main.html')


def regist(request):
   if not request.user.is_authenticated:
      return redirect('login')
   if request.method == 'POST':
      article = Article()
      article.title = request.POST['title']
      article.regist_date = request.POST['regist_date']
      article.exp_date = request.POST['exp_date']
      article.notice = request.POST['notice']
      article.price = request.POST['price']
      article.being_rented = 'x'
      article.regist_code = request.user.username #Authuser테이블의 id가져오기
      article.categorie = request.POST['categorie'] #카테고리 등록 x
      # article.categorie = request.POST('categorie')
      article.save()
      return redirect('main')
   else:
      article = Article.objects.all()
      return render(request,'app/regist.html', {'article':article})


def find_id_pwd(request):
   if request.method == 'POST':
      user = AuthUser()
      # user=AuthUser.objects.id()
      if user.undergrad == request.POST['undergrad']:
         if user.username == request.POST['username']:
            # messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')
            return redirect('login')
   else:
      return render(request,'app/find_id_pwd.html')

def search_detail(request):
   if request.method == 'POST':
      article = Article()
      # user=AuthUser.objects.id()
      if request.POST['의류']:
         return
      if article.undergrad == request.POST['undergrad']:
         if article.username == request.POST['username']:
            # messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')
            return redirect('login')
   else:
      return render(request,'app/find_id_pwd.html')



def get_queryset(self):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')
    article = Article.objects.order_by('-id') 
    
    if search_keyword :
        if len(search_keyword) > 1 :
            if search_type == 'all':
                search_article = article.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword) | Q (writer__user_id__icontains=search_keyword))
            elif search_type == 'title_content':
                search_article = article.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword))
            elif search_type == 'title':
                search_article = article.filter(title__icontains=search_keyword)    
            elif search_type == 'content':
                search_article = article.filter(content__icontains=search_keyword)    
            elif search_type == 'writer':
                search_article = article.filter(writer__user_id__icontains=search_keyword)

            return search_article
        else:
            messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
    return article

   
def get_context_data(self, **kwargs):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')

    if len(search_keyword) > 1 :
        context['q'] = search_keyword
    context['type'] = search_type

    return context


def manage(request):
   articles = Article.objects.all()
   return render(request, 'app/manage.html', {"articles":articles})

def wish(request):
   articles = Article.objects.all()
   return render(request, 'app/wish.html', {"articles":articles})

def borrow(request):
   if not request.user.is_authenticated:
      return redirect('login')
   articles = Article.objects.all()
   return render(request, 'app/borrow.html', {"articles":articles})
   