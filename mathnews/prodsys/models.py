from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#class ArticleAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("title",)}

# Create your models here.
class Article(models.Model):
    title = models.CharField('title', max_length=254, blank=True)
    slug = models.SlugField(blank=True)
    subtitle = models.CharField('byline', max_length=254, blank=True)
    body = models.TextField('article body', blank=True)
    signature = models.CharField('signature', max_length=254, blank=True)
    issue = models.ForeignKey('Issue')
    author = models.ForeignKey(User)

    def clean(self):
        from django.core.exceptions import ValidationError
        from StringIO import StringIO
        from lxml import etree
        import os
        dtd_fh = open(settings.STATIC_ROOT + 'article.dtd');
        dtd = etree.DTD(dtd_fh);
        root = etree.XML(self.body);
        if not dtd.validate(root):
            raise ValidationError("Your article body is invalid mNmL: {0}".format(dtd.error_log))#.filter_from_errors()[0]))

        #if ((author is None) or (not author.is_authenticated()) or (not author.is_active)):
        #    raise ValidationError('Author is empty, inactive, or not authenticated.');
        pass

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



