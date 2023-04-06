# from ssl import _PasswordType
from django.shortcuts import render, redirect
# from .models import Building, Employee, Visitor
from .models import User, Article, AuthUser, Contact, Photo, MileageContact
from django.views.generic.base import TemplateView
from django.contrib import auth, messages
from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from proj.settings import SECRET_KEY
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from datetime import datetime
import requests
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password
import random
import json


def index(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "63c2dd857c7b12167a030cfcec8b5674",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        params = {
            "cid": "TC0ONETIME",
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "user1009",    # 유저 아이디
            "item_name": "우산",        # 구매 물품 이름
            "quantity": "1",               # 구매 물품 수량
            "total_amount": "1200",        # 구매 물품 가격
            "tax_free_amount": "0",
            "approval_url": "http://127.0.0.1:8000/approval",
            "cancel_url": "http://127.0.0.1:8000",
            "fail_url": "http://127.0.0.1:8000",
        }
        res = requests.post(URL, headers=headers, params=params)
        #res = res.json()
        request.session['tid'] = res.json()['tid']
        # request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        # next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        next_url = res.json()['next_redirect_pc_url']
        return redirect(next_url)

    return render(request, 'app/index.html')


def approval(request):
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "63c2dd857c7b12167a030cfcec8b5674",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "1001",     # 주문번호
        "partner_user_id": request.user.username,    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),
    }
    authUsers = AuthUser.objects.get(username=request.user.username)
    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
        'adress': authUsers.adress,
    }

    return render(request, 'app/approval.html', context)


class MainpageView(TemplateView):
    template_name = 'app/main.html'


def main_view(request):
    return render(request, 'main.html')


def bui_view(request):
    users = User.objects.all()
    return render(request, 'app/bui.html', {"users": users})

##########################################


def borrow(request):
    if not request.user.is_authenticated:
        return redirect('login')
    articles = Article.objects.filter(
        exp_date__gte=datetime.now()).exclude(username=request.user.username).order_by('-ident')
    return render(request, 'app/borrow.html', {"articles": articles})


def bui(request):
    return render(request, 'app/bui.html')


def contact(request):
    return render(request, 'app/contact.html')

def changepassword(request):
    if request.method == 'POST':
        user = AuthUser.objects.get(username = request.user.username)
        # if user.password == request.POST['password']: 현재 비밀번호랑 입력한 현재비밀번호 일치여부 생략
        if request.POST['password1'] == request.POST['password2']:
            user.password = make_password(request.POST['password1'])
            user.save()
            return redirect('mypage')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('main')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'app/changepassword.html', {
        'form': form
    })


def restrictiondetailsofuse(request):
    return render(request, 'app/restrictiondetailsofuse.html')


def detail(request):
    if not request.user.is_authenticated:
        return redirect('login')
    articles = Article.objects.all()
    return render(request, 'app/detail.html', {"articles": articles})


# def login(request):
#    return render(request, 'app/login.html')


def passwdreset(request):
    return render(request, 'app/passwdreset.html')

# def regist(request):
#    return render(request, 'app/regist.html')


def rented_other_detail(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'app/rented_other_detail.html')


def search_result(request):
    return render(request, 'app/search_result.html')


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        user = AuthUser()
        if AuthUser.objects.filter(email=request.POST['email']):
            return redirect('login')
        else:
            kku = "@kku.ac.kr"
            user.email = request.POST['email'] + kku
            user.password = make_password(request.POST['password'])
            user.phone = request.POST['phone']
            # user.borrow_code = request.POST['borrow_code']
            # user.username = request.POST['username']
            user.major = request.POST['major']
            user.undergrad = request.POST['undergrad']
            user.adress = request.POST['adress']
            user.username = request.POST['username']
            user.name = request.POST['name']
            user.mileage = '0'
            user.is_superuser = '0'
            user.is_staff = '0'
            user.is_active = '0'
            user.save()
            return redirect('main')
    else:
        user = User.objects.all()
        return render(request, 'app/sign_up.html', {'user': user})


def email_check(request, email_str):
    if request.method == 'POST':
        numbers = random.randrange(1000, 9999)
        email = EmailMessage(
            '회원가입 인증번호가 발송되었습니다.',  # 이메일 제목
            '이메일 인증번호는 ' + str(numbers) + '입니다.',  # 내용
            to=[email_str+"@kku.ac.kr"],  # 받는 이메일
        )
        email.send()
        context = {'numbers': numbers}
        return HttpResponse(json.dumps(context), content_type="application/json")


def validate_email(request, email_str):
    if request.method == 'POST':
        try:
            user = get_object_or_404(AuthUser, email=email_str)
            if user != None:
                res = "이미 존재하는 이메일입니다."
        except:
            res = "사용가능한 이메일입니다."
        context = {'res': res}
        return HttpResponse(json.dumps(context), content_type="application/json")


def sign_in(request):
    return render(request, 'app/sign_in.html')


def wish_detail(request):
    return render(request, 'app/wish_detail.html')


def bui_view(request):
    users = User.objects.all()
    articles = Article.objects.all()
    return render(request, 'app/bui.html', {"users": users, "articles": articles})


def article_view(request):
    articles = Article.objects.all()
    return render(request, 'app/borrow.html', {"articles": articles})

# def login_check(request):
#    users = User.objects.all()
#    return render(request, "app/mypage.html", {"users":users})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # user = auth.authenticate(request, username=username, password=password)
        user = authenticate(username=username, password=password)
        if user is not None:  # 로그인 정보가 있다면
            # auth.login(request, user)
            auth_login(request, user)
            return redirect('main')
        else:  # 로그인 정보가 없다면
            auth_logout(request)
            return render(request, 'app/login.html', {'error': 'username or password is incorrect'})
    else:
        auth_logout(request)
        return render(request, 'app/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('bui')
    return render(request, 'main.html')


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
        article.username = request.user.username  # Authuser테이블의 id가져오기
        article.categorie = request.POST['categorie']  # 카테고리 등록
        article.tid = 0  # 카테고리 등록
        photo = Photo()
        photo.username = request.user.username
        # photo.images = request.FILES['images']
        photo.save()
        article.save()
        return redirect('manage')
    else:
        article = Article.objects.all()
        return render(request, 'app/regist.html', {'article': article})


# def mileage(request):
#    if request.method == "POSET":
#        mileage = mileage + 0.95 *


def find_id_pwd(request):
    if request.method == 'POST':
        user = AuthUser.objects.get(
            email=request.POST['email'], undergrad=request.POST['undergrad'])
        password = User.objects.make_random_password()
        user.password = make_password(password)
        user.save()
        email = EmailMessage(
            '비밀번호가 변경되었습니다.',  # 이메일 제목
            '변경된 비밀번호는 ' + password + '입니다.',  # 내용
            to=[request.POST['email']],  # 받는 이메일
        )
        email.send()
        return redirect('find_id_pwd')
    else:
        return render(request, 'app/find_id_pwd.html')


def find_id(request, studentNum, name):
    authUser = AuthUser.objects.get(undergrad=studentNum, name=name)
    return render(request, 'app/find_id_pwd.html', {'username': authUser.username})


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
        return render(request, 'app/find_id_pwd.html')


def get_queryset(self):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')
    article = Article.objects.order_by('-id')

    if search_keyword:
        if len(search_keyword) > 1:
            if search_type == 'all':
                search_article = article.filter(Q(title__icontains=search_keyword) | Q(
                    content__icontains=search_keyword) | Q(writer__user_id__icontains=search_keyword))
            elif search_type == 'title_content':
                search_article = article.filter(
                    Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
            elif search_type == 'title':
                search_article = article.filter(
                    title__icontains=search_keyword)
            elif search_type == 'content':
                search_article = article.filter(
                    content__icontains=search_keyword)
            elif search_type == 'writer':
                search_article = article.filter(
                    writer__user_id__icontains=search_keyword)

            return search_article
        else:
            messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
    return article


def get_context_data(self, **kwargs):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')

    if len(search_keyword) > 1:
        context['q'] = search_keyword
    context['type'] = search_type

    return context


def wish(request):
    articles = Article.objects.all()
    return render(request, 'app/wish.html', {"articles": articles})


def manage(request):
    articles = Article.objects.all()
    articles = articles.filter(username=request.user.username)
    return render(request, 'app/manage.html', {"articles": articles})


def mypage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # authuser = AuthUser.objects.all()
    # contact = Contact.objects.all()
    # authuser = AuthUser()
    authusers = AuthUser.objects.filter(username=request.user.username)
    # authuser.mileage=AuthUser.objects.filter(authuser=request.user.mileage)
    # mileages=Mileage.objects.filter(username=request.user.username)
    # return render(request, 'app/mypage.html', {"authusers": authusers, "mileages": mileages})
    return render(request, 'app/mypage.html', {"authusers": authusers})


def contact(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        contact = Contact()
        contact.title = request.POST['title']
        contact.email = request.POST['email']
        contact.content = request.POST['content']
        contact.date = datetime.now()
        contact.username = request.user.username  # Authuser테이블의 id가져오기
        contact.save()
        return redirect('my_contact')
    else:
        contact = Article.objects.all()
        return render(request, 'app/contact.html', {'contact': contact})


# def my_contact(request, username):
#    # print(articles)
#    contacts = get_object_or_404(Contact, username=username)
#    # articles = Article.objects.get(pk=ident)
#    # articles = get_object_or_404(Article, pk=request.GET.get('ident'))
#    # articles = Article.objects.first()
#    # print(articles.id)
#    print(contacts.title)
#    print(contacts.content)
#    return render(request, 'app/my_contact.html', {"contacts": contacts})


def my_contact(request):
    # print(articles)
    # contacts = Contact.objects.filter(username=auth.username)
    # contacts=Contact.objects.get(username=request.user.username)
    usrName = request.user.username
    contacts = Contact.objects.filter(username=request.user.username)
    print(contacts)

    return render(request, 'app/my_contact.html', {"result":{"contacts": contacts, "username": usrName}})


def withdraw(request):
    if request.method == 'POST':  # mypage의 form을 통해 POST 방식으로 전달했는지 확인
        authuser = AuthUser.objects.get(username=request.user.username)
        if authuser.state == '출금대기중':
            return redirect('main')
        else:
            authuser.state = "출금대기중"
        authuser.save()
        mileage_contact = MileageContact()
        mileage_contact.bank = request.POST['bank']
        mileage_contact.account_number = request.POST['account_number']
        mileage_contact.price = request.POST['price']
        mileage_contact.username = request.user.username  # Authuser테이블의 id가져오기
        mileage_contact.email = request.user.email  # Authuser테이블의 email가져오기
        mileage_contact.phone = request.POST['phone']
        mileage_contact.save()
        return redirect('my_withdraw')
    else:
        mileages = AuthUser.objects.filter(username=request.user.username)
        return render(request, 'app/withdraw.html', {"mileages": mileages})


def my_withdraw(request):
    # print(articles)
    # contacts = Contact.objects.filter(username=auth.username)
    # contacts=Contact.objects.get(username=request.user.username)
    my_withdraws = MileageContact.objects.filter(
        username=request.user.username)

    return render(request, 'app/my_withdraw.html', {"my_withdraws": my_withdraws})


def what_i_borrowed(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # articles = Article.objects.all().order_by('-ident')
    # articles=Article.objects.filter(username=request.user.username)
    articles = Article.objects.filter(being_rented=request.user.username)
    return render(request, 'app/what_i_borrowed.html', {"articles": articles})


def borrow_detail(request, ident):
    # print(articles)
    articles = get_object_or_404(Article, ident=ident)
    # photos = get_object_or_404(Photo, ident=ident)
    # photos = Photo.objects.all()
    # articles = Article.objects.get(pk=ident)
    # articles = get_object_or_404(Article, pk=request.GET.get('ident'))
    # articles = Article.objects.first()
    # print(articles.id)ㄴ
    print("borrow_detail!")
    print(articles.title)
    print(articles.ident)
    print(articles.exp_date)
    print(articles.notice)
    print(articles.categorie)
    print(articles)
    if request.method == "POST":
        print("post!")
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "63c2dd857c7b12167a030cfcec8b5674",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        params = {
            "cid": "TC0ONETIME",
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": request.user.username,    # 유저 아이디
            "item_name": articles.title,        # 구매 물품 이름
            "item_author": articles.username,  # 물품 등록자명
            "quantity": "1",                # 구매 물품 수량
            "total_amount": articles.price,        # 구매 물품 가격
            "tax_free_amount": "0",
            "approval_url": "http://127.0.0.1:8000/approval",
            "cancel_url": "http://127.0.0.1:8000",
            "fail_url": "http://127.0.0.1:8000",
        }
        res = requests.post(URL, headers=headers, params=params)
        #res = res.json()
        request.session['tid'] = res.json()['tid']
        # request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        # next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        next_url = res.json()['next_redirect_pc_url']

        addMileage = articles.price * 0.95
        productAuthor = AuthUser.objects.get(username=articles.username)
        if productAuthor.mileage == None or productAuthor.mileage == "":
            productAuthor.mileage = str(addMileage)
            productAuthor.save()
        else:
            productAuthor.mileage = str(
                int(productAuthor.mileage) + addMileage)
            productAuthor.save()
        articles.being_rented = request.user.username
        articles.save()

        return redirect(next_url)
    return render(request, 'app/borrow_detail.html', {"articles": articles})


def what_i_borrowed_detail(request, ident):
    articles = get_object_or_404(Article, ident=ident)
    return render(request, 'app/what_i_borrowed_detail.html', {"articles": articles})


def manage_detail(request, ident):
    articles = get_object_or_404(Article, ident=ident)
    return render(request, 'app/manage_detail.html', {"articles": articles})


def search(request):
    articles = Article.objects.all().order_by('-ident')

    q = request.POST.get('q', "")

    print(q)

    if q:
        articles = articles.filter(title__icontains=q)
        return render(request, 'app/borrow.html', {'articles': articles, 'q': q})

    else:
        return render(request, 'app/borrow.html')


def change_persnal(request):
    if request.method == 'POST':
        user = AuthUser.objects.get(username=request.user.username)
        # user.email = request.POST['email']
        user.password = make_password(request.POST['password'])
        user.phone = request.POST['phone']
        # user.borrow_code = request.POST['borrow_code']
        # user.username = request.POST['username']
        user.major = request.POST['major']
        # user.undergrad = request.POST['undergrad']
        user.adress = request.POST['adress']
        # user.username = request.POST['username']
        # user.name = request.POST['name']
        user.is_superuser = '0'
        user.is_staff = '0'
        user.is_active = '0'
        user.save()
        return redirect('main')
    else:
        authuser = AuthUser.objects.get(username=request.user.username)
        return render(request, 'app/change_persnal.html', {"authuser": authuser})


def edit_myarticle(request, ident):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        article = Article.objects.get(ident=ident)
        article.username = request.user.username  # Authuser테이블의 id가져오기
        article.title = request.POST['title']
        article.regist_date = request.POST['regist_date']
        article.exp_date = request.POST['exp_date']
        article.notice = request.POST['notice']
        article.price = request.POST['price']
        article.being_rented = 'x'
        article.categorie = request.POST['categorie']  # 카테고리 등록
        article.tid = 0  # 카테고리 등록
        photo = Photo()
        photo.username = request.user.username
        # photo.images = request.FILES['images']
        photo.save()
        article.save()
        return redirect('manage')
    else:
        article = Article.objects.get(ident=ident)
        return render(request, 'app/edit_myarticle.html', {'article': article})
