from django.urls import path
from produto import views as v

app_name = 'produto'

urlpatterns = [
    path('', v.produto_list, name='produtos_list'),
    path('<int:pk>/', v.produto_detail, name='produto_detail'),
]