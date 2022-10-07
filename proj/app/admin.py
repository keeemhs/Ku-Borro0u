from django.contrib import admin
from .models import *
from rangefilter.filter import DateRangeFilter, DateRangeFilter

# Register your models here.
#admin.site.register(Employee)
#admin.site.register(Building)
#admin.site.register(Visitor)
# admin.site.register(Article)
# admin.site.register(User)

#from django.contrib.admin.models import LogEntry   // clear admin recent actions
#LogEntry.objects.all().delete()

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'regist_date', 'exp_date'] # 커스터마이징 코
    list_filter = ['title', 'regist_date', 'exp_date']
    list_per_page = 7
    search_fields = ['empname', 'floor', 'uniname']
admin.site.register(Article, ArticleAdmin)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['email', 'password', 'phone', 'regis_date', 'borrow_code', 'regist_code'] # 커스터마이징 코
#     list_filter = ['email', 'password', 'phone', 'regis_date', 'borrow_code', 'regist_code']
#     list_per_page = 7
#     search_fields = ['email', 'password', 'phone', 'regis_date', 'borrow_code', 'regist_code']
# admin.site.register(User, UserAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'password', 'phone', 'username'] # 커스터마이징 코
    list_filter = ['email', 'password', 'phone', 'username']
    list_per_page = 7
    search_fields = ['email', 'password', 'phone', 'username']
admin.site.register(AuthUser, UserAdmin)



# class VisitorAdmin(admin.ModelAdmin):
#     list_display = ['visname', 'viscode', 'temp', 'uniname', 'visfloor'] # 커스터마이징 코
#     list_filter = ['visname', 'viscode', 'temp', 'uniname', 'visfloor']
#     list_per_page = 7
#     search_fields = ['visname', 'viscode', 'temp', 'uniname', 'visfloor']
# admin.site.register(Visitor, VisitorAdmin)


#class EmployeeAdmin(admin.ModelAdmin):
#    list_display = ['empname', 'floor', 'uniname']
#    list_filter = ('gender',
#        ('hire_date', DateRangeFilter),
#        ('birth_date', DateRangeFilter),
#    )
#    search_fields = ['empname', 'floor', 'uniname']