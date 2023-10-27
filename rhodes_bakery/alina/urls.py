from django.urls import path
import alina.views as views
import alina.viewpro.main_page as mains
import alina.viewpro.logins as log

app_name = 'alina'
urlpatterns = [
    path('', views.hello),
    path('m_page/', mains.mian_page),
    path('login/list/', log.login_list),
    path('login/add/', log.login_add),
    path('login/logins/', log.logins),
    path('login/delete/<int:nid>/', log.login_delete),
    path('login/edit/<int:nid>/', log.login_edit),
    path('login/edit/name/', log.login_edit_name),
    path('login/out/', log.login_out),
]
