import xadmin
from django.urls import path
from lists import views

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',views.home_page,name='home')
]
