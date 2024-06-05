from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('getuser/<str:name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"), 
    # re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item)
    path("home/",views.form_view, name="home"),
    path("about/", views.about),
    path('menu_card/',views.menu_by_id),
    path('index/',views.index)
]
