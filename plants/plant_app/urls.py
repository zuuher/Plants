from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("/home", views.home, name="home"),
    path("", views.LOGIN, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("plant/", views.add_plant, name="plant"),
    path("about/", views.about, name="about"),
    path('signup/', views.signup, name='signup'),
    path('details/<int:plan_id>/', views.edit_plant, name='details'),

   path('delete/<int:plan_id>/', views.delete_plant, name='delete_plant'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)