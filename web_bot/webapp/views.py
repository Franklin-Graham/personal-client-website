from django.shortcuts import render, get_object_or_404
from . models import Detail,Telegram_project,Github_project,Account
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def fun1(request,id=None):
    obj_1 = Detail.objects.all()
    obj_2 = Telegram_project.objects.all()
    obj_3 = Github_project.objects.all()
    obj_4 = Account.objects.all()
    return render(request,'index.html',{'object_1':obj_1,'object_2':obj_2,'object_3':obj_3,'object_4':obj_4})