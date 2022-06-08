
from django.contrib import admin
from django.urls import path, include
from test01 import views
from django.conf.urls import url

urlpatterns = [

    # path("create/",views.create),
    # path('read/<id>/', views.read),
    # path('delete/',views.delete),
    # path('update/<id>/',views.update),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^api/data/$',views.get_data, name='api-data'),
    url(r'^api/chart/data/$',views.ChartData.as_view()),
    url(r'^stockofnaver/$',views.NaverHome.as_view()),
    url(r'^stockoflg/$',views.LGHome.as_view()),
    url(r'^stockofkakao/$',views.KakaoHome.as_view()),


]

