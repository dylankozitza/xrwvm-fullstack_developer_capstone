# Uncomment the imports before you add the code
# 
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# 
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path(route='register', views=views.registration, name='register'),
   # path('registration', views.registration, name='registration'),

    # path for login
    path(route='login', view=views.login_user, name='login'),
    #path('login', views.login_user, name='login'),

    # path for logout
    path(route='logout/', views=views.logout_request, name='logout'),
    #path('logout/', views.logout_request, name='logout'),
    
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
