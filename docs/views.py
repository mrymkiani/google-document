
from django.shortcuts import render , HttpResponse
from .models import Document
from .forms import DocumentForm
from .serializer import DocumentSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass


class DocumentList(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Document.objects.filter(user = self.request.user)    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["created_at" , "updated_at"]
    search_fields = ["title"]
    
    
class DocumentEdit(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Document.objects.filter(user = self.request.user)    

def DocumentDownload(request, pk):
    document = Document.objects.get( pk=pk, user=request.user)
    response = HttpResponse(document.file.read(), content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{document.title}"'
    return response
