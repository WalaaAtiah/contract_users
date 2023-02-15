from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Client
from .permissions import IsOwnerOrReadOnly
from .serializers import ClientSerializer
from django.urls import reverse_lazy

class ClientList(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
