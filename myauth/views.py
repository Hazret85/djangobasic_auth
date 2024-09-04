from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def read_cookie_view(request):
    cookie_value = request.COOKIES.get('my_cookie', 'Значение по умолчанию')
    return HttpResponse(f'Cookie value: {cookie_value}')


def set_cookie_view(request):
    response = HttpResponse('Cookie установлено!')
    response.set_cookie('my_cookie', 'Some value')
    return response

def read_session_view(request):
    session_value = request.session.get('my_session_key', 'Значение по умолчанию')
    return HttpResponse(f'Session value: {session_value}')


def set_session_view(request):
    request.session['my_session_key'] = 'Some value'
    return HttpResponse('Session установлено!')
