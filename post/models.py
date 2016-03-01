from django.db.models import *
from django.core.urlresolvers import reverse


class Category(Model):
    
    title = CharField(max_length=128)
    slug = SlugField()
    description = TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])
    
    
class Post(Model):
    
    title = CharField(max_length=128)
    slug = SlugField()
    categories = ManyToManyField(Category, blank=True)
    image = ImageField(upload_to='media/posts/', blank=True, null=True)
    excerpt = TextField(blank=True, null=True)
    content = TextField()
    
    created = DateTimeField(auto_now_add=True)
    published = DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_single', args=[self.slug])
    
    def has_next(self):
        return Post.objects.filter(published__lt=self.published).order_by('-published').count()
    
    def next_post(self):
        return Post.objects.filter(published__lt=self.published).order_by('-published')[0]
    
    def has_previous(self):
        return Post.objects.filter(published__gt=self.published).order_by('published').count()
    
    def previous_post(self):
        return Post.objects.filter(published__gt=self.published).order_by('published')[0]