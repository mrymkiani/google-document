from django.urls import path
from .views import DocumentEdit , DocumentList , DocumentDownload

urlpatterns = [
    path('doc-list-create' ,DocumentList.as_view() ),
    path('edit-docs/<int:pk>',DocumentEdit.as_view() ),
    path('download/<int:pk>/', DocumentDownload),
]