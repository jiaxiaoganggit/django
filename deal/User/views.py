from django.shortcuts import render

# Create your views here.
def regist(request):
    return render(request, 'HDdeal_user/regist.html')