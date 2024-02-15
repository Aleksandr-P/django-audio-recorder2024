from django.conf import settings
from django.urls import re_path, path
from django.conf.urls.static import static

from .views import AudioFileAPICreateView, AudioFileCRUDCreateView
from audio_files import views

urlpatterns = [
    path('audio-files', AudioFileCRUDCreateView.as_view(), name='audio-file-crud-create'),
    path('audio-files/new', AudioFileAPICreateView.as_view(create_field='audio_file'), name='audio-file-api-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
