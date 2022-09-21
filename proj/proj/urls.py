from django.contrib import admin
from django.urls import path, include
from app import views as ap

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('all/', ap.db_view),
    # path('vis/', ap.vis_view),
    # path('bui/', ap.bui_view),
    # path('emp/', ap.emp_view),
    path('', include('app.urls')),
]