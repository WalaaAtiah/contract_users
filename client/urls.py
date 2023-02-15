from django.urls import path
from .views import ClientList,ClientDetail

urlpatterns = [
    path('list', ClientList.as_view(), name='client_list'),
    path('<int:pk>/', ClientDetail.as_view(), name='client_detail')
]

