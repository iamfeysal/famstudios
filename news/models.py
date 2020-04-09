from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(db_index=True, max_length=150, primary_key=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    description = RichTextField(max_length=350, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True, config_name='special')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')
    click_nums = models.IntegerField(default=0, verbose_name=u'Clicks')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The specific manager.

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])
