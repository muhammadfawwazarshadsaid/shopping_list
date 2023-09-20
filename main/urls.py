from django.urls import path
from main.views import show_json, show_main, create_product, show_xml 
from main.views import register #sesuaikan dengan nama fungsi yang dibuat

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('json/', show_json, name='show_json'), 
    path('register/', register, name='register'), 



    
]