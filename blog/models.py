from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from extensions.utils import jalali_convert
class Article_manager(models.Manager):
    def published(self):
        return self.filter(status='p')
class Category(models.Model):
    title=models.CharField(max_length=20,verbose_name='دسته بندی ')
    status=models.BooleanField(default=True,verbose_name='وضعیت ')
    slug=models.SlugField(max_length=12,unique=True,verbose_name='شماره ')

    class Meta:
        verbose_name_plural='دسته بندی های من '
    def __str__(self):
        return self.title


class Artile(models.Model):
    STATUS_CHOIC=(
        ('l','چاپ شده'),('n','چاپ نشده '),
    )
    name=models.CharField(max_length=20,verbose_name='اسم نویسنده ')
    category=models.ManyToManyField(Category,verbose_name='دسته بندی',related_name='article')
    title=models.CharField(max_length=30,verbose_name='نام عنوان')
    image = models.ImageField(upload_to='images',verbose_name='تصویر')
    description=models.TextField(verbose_name='ایجاد متن')
    status=models.CharField(max_length=1,choices=STATUS_CHOIC,verbose_name='وضعیت')
    publish=models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')

    slug=models.SlugField(max_length=12,unique=True)
    class Meta:
        verbose_name_plural='نظرات من'
        ordering=['-publish']

    def __str__(self):
        return self.title
    def jalali_publish(self):
        return jalali_convert(self.publish)

    objects=Article_manager()
class testy(models.Model):
    test_passage=models.CharField(max_length=16,null=True,blank=False)
    Username=models.ForeignKey(User,null=True,related_name='username')
    slug=models.SlugField(unique=True)
    