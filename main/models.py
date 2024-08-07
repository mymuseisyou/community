from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

#게시글 모델
class Post(models.Model):
    postname = models.CharField(max_length=50)
    username = models.CharField(max_length=10, blank=True, null=True)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    #contents = CKEditor5Field(config_name='extends')
    contents = CKEditor5Field(blank=True, null=True)
    
    #postname이 포스트오브젝트 대체하는거
    def __str__(self):
        return self.postname