from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from learn.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
class UserForm(forms.Form):
    Username=forms.CharField(label='',max_length=30)
    PassWord=forms.CharField(max_length=30)
    #Level=forms.IntegerField()
def index(request):
    return HttpResponse(u'dhdhdh')
#@login_required
def test(request):
    return render(request,'test.html')
def inner(request):
    return render(request,'src')
def inner1(request):
    return render(request,'sr')
def login(request):
    return render(request,'login.html')
def judge(request):
    req=request.POST
    username=req.get('username')
    password=req.get('password')
    userpass=User.objects.filter(Username__exact=username,PassWord__exact=password)
    #userpass=authenticate(username=username,password=password)
    if userpass:
        response=HttpResponseRedirect('/type')
        response.set_cookie('cookie_username',username,3000)
        return response
    else:
        return HttpResponse(u'<h1>用户名/密码错误</h1>')
def regist(request):
    req=request.POST
    print(req)
    username=req.get('userid')
    password=req.get('psw')
    print(username,password)
    registjudge=User.objects.filter(Username__exact=username)
    print(registjudge)
    if registjudge:
        return HttpResponse(u'<h1>用户名已存在</h1>')
    else:
        User.objects.create(Username=username,PassWord=password)
        print(username,password)
        return HttpResponse(u'注册成功')
    return render(request,'login.html')
def type(req):
    return render(req,'type.html')
def choose(req):
    return render(req,'choose.html')



# Create your views here.
