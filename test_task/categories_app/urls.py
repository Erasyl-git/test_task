from django.urls import path
from .views import *


urlpatterns = [
    path('', Categories, name='home'), 
    path('categories/', Categories, name='categories'),
    path('subcategory/<int:pk>/', Subcategorydetail, name='subcategory'), 
]

#ну если тут было бы не функция ,а класс то юзули бы .as_view() 