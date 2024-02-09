
from django.urls import path
from . import views
urlpatterns = [
   path('',views.homePage,name = 'index'),
   path('question/<int:id>', views.questionPage, name='question'),
   path('register', views.registerPage, name='register'),
   path('login/', views.loginPage, name='login'),
   path('logout', views.logoutPage, name='logout'),
   path('new-question', views.newQuestionPage, name='new-question'),
   path('reply', views.replyPage, name='reply'),
   # path('profile ',views.profile,name = 'profile')/
]
