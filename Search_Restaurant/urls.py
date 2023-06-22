from django.urls import path
from appname import views

app_name = 'appname'

urlpatterns = [
    path('search/', views.search_form_view, name='search'),
    path('results/<str:query>/', views.results_view, name='results'),
]
