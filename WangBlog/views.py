from django.shortcuts import render
from WangBlog.models import *
# Create your views here.


def hello(request):
    name = "wangtieguo"
    return render(request, "index.html", locals())
    # return HttpResponse("<h1>hello world, 我是王铁锅</h1>")


def login(request):
    print('hello')
    if "POST" == request.method:
        print('hello0')
        uf = UserForm(request.POST, request.FILES)
        print('hello0.5')
        if uf.is_valid():
            print('hello11')
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            print(username)
            print(password)
            print(email)
            success = User.objects.filter(username=username, password=password, email=email)
            print('hello1')
            if success:
                print('hello2')
                return render(request, "index.html", {'username': username})
            else:
                print('hello3')
                return render(request, "login.html", locals())
        else:
            print('hello22')
    else:
        uf = UserForm()
    print('hello4')
    return render(request, "login.html", locals())


def register(request):
    if "POST" == request.method:
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            img = uf.cleaned_data['img']
            print(username)
            print(password)
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.img = img
            user.save()
            return render(request, "login.html", {'username': username})
    else:
        uf = UserForm()
    return render(request, "register.html", {'uf': uf})
