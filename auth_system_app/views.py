from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth



def home(request):
    context = {}
    if request.user.is_authenticated:
        context['userStatus'] = 'zalogowany'
    else:
        context['userStatus'] = 'Zaloguj się aby zobaczyć więcej!'

    # if not Week.objects.exists():                           #Sprawdzam istnienie 24 tygodni w bazie
    #     for week_number in range(1, 25):                    #używam metody creat do ich stworzenia
    #         Week.objects.create(week_number=week_number)

    # weeks = Week.objects.order_by('week_number')[:24]       #dodaje im liczy 24
    # weeks_list = [{'id': week.id, 'week_number': week.week_number} for week in weeks] #litruje aby uzyska id tygodnia
    context['weeks'] = list(range(1, 25))                            # Dodanie listy tygodni do kontekstu

    return render(request,
                  'auth_app/home.html',
                  context)

def signup_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")

        if User.objects.filter(username=username).exists():
            context = {'error': 'Taki użytkownik już istnieje! Proszę podać inną nazwę użytkownika.'}
            return render(request, 'auth_app/signup.html', context)

        user = User.objects.create_user(username=username,
                                        password=password1,
                                        email=email,
                                        first_name=firstname,
                                        last_name=lastname)
        login(request, user)
        return redirect('auth_app:home')

    return render(request, 'auth_app/signup.html')


def login_views(request):
    context = {}
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None:
            auth.login(request,
                       user)
            return redirect('auth_app:home')
        else:
            context['error'] = 'Podane hasło lub login są błędne!.'
            return render(request,
                          'auth_app/login.html',
                          context)
    else:
        return render(request,
                      'auth_app/login.html')


def logout_views(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('auth_app:home')


