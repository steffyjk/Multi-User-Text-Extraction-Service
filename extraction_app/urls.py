from django.urls import path
from .views import ExtractTextView, DocumentUploadView, ExtractAndStoreTextView

urlpatterns = [
    path('upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('extract-text/', ExtractTextView.as_view(), name='extract-text'),

    # extra
     path('extract-and-store/', ExtractAndStoreTextView.as_view(), name='extract-and-store'),
]