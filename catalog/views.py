import face_recognition
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import RecognitionForm

from .models import Photo



def recognize(request):
    if request.method == 'POST':

        form = RecognitionForm(request.POST, request.FILES)
        to_recognize = request.FILES['to-recognize']
        print(form.is_valid())
        # if form.is_valid():
        if request.method == 'POST':
    
            res = False
            founded_name = ''
            known_images = Photo.objects.all()
            known_image = None
            
            unknown_image = face_recognition.load_image_file(to_recognize)
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            i = 0

            while(not res and i <= len(known_images)):
                known_image = face_recognition.load_image_file(known_images[i].get_photo())
                known_encoding = face_recognition.face_encodings(known_image)[0]

                res = face_recognition.compare_faces([known_encoding], unknown_encoding)[0]
                print(res, i)
                
                if res:
                    founded_name = known_images[i].get_name()
                i += 1
            
            print(founded_name)
    
    return render(request, 'catalog/recognize.html')



# def index(request):


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
    fields = ['name', 'bio']
    initial = {'bio': 'Bio has not been added yet.'}


class PhotoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.moderator_required'
    
    model = Photo
    fields = ['name', 'bio']
    success_url = reverse_lazy('photos')


class PhotoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.moderator_required'
    
    model = Photo