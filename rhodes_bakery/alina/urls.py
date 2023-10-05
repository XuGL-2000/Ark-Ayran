from django.urls import path
import alina.views as views
import alina.viewpro.main_page as mains
import alina.viewpro.logins as log

app_name = 'alina'
urlpatterns = [
    path('', views.hello),
    path('m_page/', mains.mian_page),

    path('login/', log.register),
]
