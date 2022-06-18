import face_recognition
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import RecognitionForm

from .models import Photo



def index(request):
    founded_name = ''
    
    form = RecognitionForm(request.POST, request.FILES)
    if request.method == 'POST':

        if form.is_valid():
    
            res = False
            known_images_lst = Photo.objects.all()
            known_image = None
            
            unknown_image = face_recognition.load_image_file(request.FILES['to_recognize'])
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            i = 0

            while(i <= len(known_images_lst)):
                known_image = face_recognition.load_image_file(known_images_lst[i].get_photo())
                known_encoding = face_recognition.face_encodings(known_image)[0]

                res = face_recognition.compare_faces([known_encoding], unknown_encoding)[0]
                
                if res:
                    founded_name = f'The result: {known_images_lst[i].get_name()}'
                    break

                i += 1

            if not res:
                founded_name = 'The result: not found'
    
    return render(request, 'catalog/index.html', {'founded_name': founded_name, 'form': form})



class PhotosListView(ListView):
    model = Photo
    paginate_by = 20


class PhotoDetailView(DetailView):
    model = Photo



class InexactListView(ListView):
    model = Photo
    template_name = 'catalog/photos_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Photo.objects.filter(status__exact='inexact identification')


class ExactListView(ListView):
    model = Photo
    template_name = 'catalog/photos_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Photo.objects.filter(status__exact='exact identification')



class PhotoCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.moderator_required'
    
    model = Photo
    fields = ['name', 'bio', 'photo']
    initial = {'bio': 'Bio has not been added yet.'}
    extra_context = {'title': 'Add person'}


class PhotoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.moderator_required'
    
    model = Photo
    fields = ['name', 'bio', 'photo']
    success_url = reverse_lazy('photos')
    extra_context = {'title': 'Edit record'}


class PhotoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.moderator_required'
    
    model = Photo