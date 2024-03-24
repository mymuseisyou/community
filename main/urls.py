from django.urls import path
from .views import *
# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

app_name='main'

urlpatterns=[
    path('',community),
    path('community/',community),
    path('community/<int:pk>/', posting, name="posting"),
    path('community/newpost/', newpost),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)