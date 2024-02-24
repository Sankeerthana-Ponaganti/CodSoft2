from django.urls import path
from . import views
from django.conf.urls.static import static
from project import settings
urlpatterns = [
      path('', views.home, name='home'),
    path('play/<str:choice>/', views.play, name='play'),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)