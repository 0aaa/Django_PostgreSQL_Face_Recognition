from django.urls import path
from .views import ExactListView, InexactListView, PhotoCreate, PhotoDelete, PhotoDetailView, PhotoUpdate, PhotosListView, index


urlpatterns = [
    path('', index, name='index'),
    
    path('photos/', PhotosListView.as_view(), name='photos'),
    path('photos/<int:pk>', PhotoDetailView.as_view(), name='photo-detail'),

    path('inexact/', InexactListView.as_view(), name='inexact'),
    path('exact/', ExactListView.as_view(), name='exact'),

    path('photos/create/', PhotoCreate.as_view(), name='photo-create'),
    path('photos/<int:pk>/update/', PhotoUpdate.as_view(), name='photo-update'),
    path('photos/<int:pk>/delete/', PhotoDelete.as_view(), name='photo-delete'),
]