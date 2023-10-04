from django.contrib import admin
from django.urls import path
from GKB_Assignment import views
from .views import Data_entry

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Data_entry.signup, name='signup'),
    path('Your_details', Data_entry.Your_details, name='Your_details'),
]
