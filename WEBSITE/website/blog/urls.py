from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.allpost,name= "allpost"),
    path('<int:blog_id>/', views.details,name= "detail"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)