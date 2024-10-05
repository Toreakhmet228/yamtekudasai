from django.contrib import admin
from django.urls import path
from main_page.views import home, get_datas

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='home'),
    path("get_data/",get_datas,name='data')
]
