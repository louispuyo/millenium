from django.urls import path
from .views import logout_user, home, LoginPageView, SignUpView, chat, room, checkview, getMessages, send


urlpattern = [
    # authentification
    path('logout/', logout_user, name='logout'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('signup/', SignUpView.as_view(template_name='signup.html'), name="signup"),

    path('', chat, name="chat"),
    path('send', send , name ="send"),

    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name="checkview"),
    path('getMessages/<str:room>/', getMessages , name ="getMessages"),
    
    ]
