
from django.contrib import admin
from django.urls import path, include
from test01 import views
from django.conf.urls import url

urlpatterns = [

    path("create/",views.create),
    path('read/<id>/', views.read),
    path('delete/',views.delete),
    path('update/<id>/',views.update),
    # path('send_data/', views.send_data, name = 'send_data'),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^api/data/$',views.get_data, name='api-data'),
    url(r'^api/chart/data/$',views.ChartData.as_view()),
]

