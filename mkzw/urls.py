from django.contrib import admin
from django.urls import path
from links import views as views_from_links

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allslinks/', views_from_links.home_links),

]
