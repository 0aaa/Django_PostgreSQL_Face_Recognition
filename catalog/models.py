from django.db.models import CharField, FileField, ForeignKey, Model, SET_NULL
from django.contrib.auth.models import User
from django.urls import reverse


class Photo(Model):
    photo = FileField(upload_to='catalog/static/images/known', max_length=50, help_text="Enter a person's photo")
    name = CharField(unique=True, max_length=50, help_text="Enter a person's name.")
    bio = CharField(max_length=200, help_text="Enter a person's bio.")

    uploaded_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)

    STATUS = (('exact', 'exact identification'), ('inexact', 'inexact identification'))

    status = CharField(max_length=30, choices=STATUS, blank=True, default='inexact identification'
                                , help_text='Measure of identification exactness.')
    
    class Meta:
        permissions = ('moderator_required', 'Set user as moderator'),
        ordering = ['name']
    
    def get_photo(self):
        t = self.photo.path.split('\\')[-1]
        return t
        
    def get_name(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a particular record."""
        return reverse('photo-detail', args=[str(self.id)])