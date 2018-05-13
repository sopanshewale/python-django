from django.urls import path, re_path
from . import views
urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('records/', views.records, name='record'),
    path('iris/', views.iris, name='iris'),
    path('calculator/', views.calculate, name='sample_cal'),
    path('simple_upload/', views.simple_upload, name='file_upload'),
    path('trecords2003/', views.special_case_2003),
    re_path(r'^trecords/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^trecords/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^trecords/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]
