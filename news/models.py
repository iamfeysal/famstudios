from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone
from django.db import models
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(
            status='published')


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='photos', blank=True, null=True)
    description = RichTextField(max_length=350, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True, config_name='special')
    publish = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 default="General")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The specific manager.

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year,
                                            self.publish.strftime('%m'),
                                            self.publish.strftime('%d'),
                                            self.slug])
