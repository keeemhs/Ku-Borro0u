from django.contrib import admin
from django.urls import path, include
from app import views as ap
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
# from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('all/', ap.db_view),
    # path('vis/', ap.vis_view),
    path('bui/', ap.bui_view, name='bui'),
    path('', ap.main_view, name='main'),
    path('borrow/', ap.borrow, name='borrow'),
    path('contact/', ap.contact, name='contact'),
    path('detail/', ap.detail, name='detail'),
    path('find_id_pwd/', ap.find_id_pwd, name='find_id_pwd'),
    path('login/', ap.login, name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    # path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('mypage/', ap.mypage, name='mypage'),
    path('passwdreset/', ap.passwdreset, name='passwdreset'),
    path('regist/', ap.regist, name='regist'),
    path('rented_other_detail/', ap.rented_other_detail, name='rented_other_detail'),
    path('search_result/', ap.search_result, name='search_result'),
    path('sign_up/', ap.sign_up, name='sign_up'),
    path('sign_in/', ap.sign_in, name='sign_in'),
    path('wish_detail/', ap.wish_detail, name='wish_detail'),
    path('logout/', ap.logout, name='logout'),
    path('manage/', ap.manage, name='manage'),
    path('wish/', ap.wish, name='wish'),
    path('', include('app.urls')),
    # +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    # path('login/', ap.LoginView.as_view(), name='login'),
    # path('logout/', ap.LogoutView.as_view(), name='logout'),
    # path("accounts/",include('accounts.urls'))
]