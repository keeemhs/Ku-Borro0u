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
    path('changepassword/', ap.changepassword, name='changepassword'),
    path('restrictiondetailsofuse/', ap.restrictiondetailsofuse, name='restrictiondetailsofuse'),
    # path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    # path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('mypage/', ap.mypage, name='mypage'),
    path('passwdreset/', ap.passwdreset, name='passwdreset'),
    path('regist/', ap.regist, name='regist'),
    path('rented_other_detail/', ap.rented_other_detail, name='rented_other_detail'),
    path('search_result/', ap.search_result, name='search_result'),
    path('sign_up/', ap.sign_up, name='sign_up'),
    path('sign_in/', ap.sign_in, name='sign_in'),
    path('wish_detail/<int:ident>/', ap.wish_detail, name='wish_detail'),
    path('logout/', ap.logout, name='logout'),
    path('manage/', ap.manage, name='manage'),
    path('manage_detail/<int:ident>/', ap.manage_detail, name='manage_detail'),
    path('borrow_detail/<int:ident>/', ap.borrow_detail, name='borrow_detail'),
    path('wish/', ap.wish, name='wish'),
    path('contact/', ap.contact, name='contact'),
    path('my_contact', ap.my_contact, name='my_contact'),
    path('what_i_borrowed', ap.what_i_borrowed, name='what_i_borrowed'),
    path('what_i_borrowed_detail/<int:ident>/', ap.what_i_borrowed_detail, name='what_i_borrowed_detail'),
    path('', include('app.urls')),
    path('search/', ap.search, name="search"),
    path('index/', ap.index, name='index'),
    # path('/', include('django.contrib.auth.urls')),
    # +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path('borrow_detail/', ap.detail, name="borrow_detail"),




    # path('login/', ap.LoginView.as_view(), name='login'),
    # path('logout/', ap.LogoutView.as_view(), name='logout'),
    # path("accounts/",include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       