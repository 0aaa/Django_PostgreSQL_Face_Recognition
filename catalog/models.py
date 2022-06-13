from django.db.models import CharField, FileField, ForeignKey, Model, SET_NULL
from django.contrib.auth.models import User


class Photo(Model):
    photo = FileField(upload_to='static/images', help_text="Enter a person's photo")
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
        return self.photo
        
    def get_name(self):
        return self.name