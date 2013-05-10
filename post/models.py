from django.db import models
from django.core.urlresolvers import reverse
from djangotoolbox.fields import ListField, EmbeddedModelField

class Posts(models.Model):
    created_at = models.DateTimeField (auto_now_add=True,db_index=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField()
    comments = ListField(EmbeddedModelField('comment'), editable=False)

    def get_absolute_url(self):
       return reverse('post', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title

class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(verbose_name="Comment")
    author = models.CharField(verbose_name="Name", max_length=255)

