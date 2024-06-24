from django.shortcuts import render, redirect
from django.http import HttpResponse


from designer.models import Designer
from investor.models import Investor
from user.models import CustomUser
#from django.http import HttpResponse, HttpRequest

def start_page(request):
    return render(request, "first_base_page.html", {})

def help_page(request):
    return render(request, "help.html", {})

def entry(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Проверка существования пользователя с указанными учетными данными
        user = None
        if CustomUser.objects.filter(email=email, password=password).exists():
            user = CustomUser.objects.get(email=email, password=password)
        elif Designer.objects.filter(email=email, password=password).exists():
            user = Designer.objects.get(email=email, password=password)
        elif Investor.objects.filter(email=email, password=password).exists():
            user = Investor.objects.get(email=email, password=password)
        
        if user:
            # Стартуем новую сессию и сохраняем в ней pk пользователя
            request.session['user_pk'] = user.pk
            
            # Редирект на соответствующую страницу в зависимости от типа пользователя
            if isinstance(user, CustomUser):
                return redirect("http://127.0.0.1:8000/user/")
            elif isinstance(user, Designer):
                return redirect("http://127.0.0.1:8000/designer/")
            elif isinstance(user, Investor):
                return redirect("http://127.0.0.1:8000/investor/")
        else:
            return HttpResponse("Неверный email или пароль")
    else:
        return render(request, "entry.html")



