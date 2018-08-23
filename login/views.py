from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

user_list = []


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # # print(username, password)
        # # temp = {'user': username, 'pwd': password}
        # user_list.append(temp)

        models.UserInfo.objects.create(user=username, pwd=password)
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})
    # return HttpResponse("hello zhaomeng")

# Create your views here.
