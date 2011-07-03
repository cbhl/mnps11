from django.db import models
from django.contrib.auth.models import User;

#class ArticleAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("title",)}

# Create your models here.
class Article(models.Model):
    title = models.CharField('title', max_length=254)
    slug = models.SlugField()
    subtitle = models.CharField('byline', max_length=254)
    body = models.TextField('article body')
    signature = models.CharField('signature', max_length=254)
    issue = models.ForeignKey('Issue')
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.slug;

class Issue(models.Model):
    slug = models.SlugField()
    volume = models.IntegerField()
    issue = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    cover_image = models.ImageField('cover image', upload_to='images/covers/%Y/%m/%d',blank=True)
    cover_caption = models.CharField('cover caption', max_length=254,blank=True)
    def __unicode__(self):
        return self.slug;



