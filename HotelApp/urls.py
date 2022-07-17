from xml.dom.minidom import Document
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *



urlpatterns = [
   
    path('adminpanel/', adminpanel, name='adminpanel'),
    path('adminpanel/collections', CollectionsandRooms, name='collectionsandrooms'),
    path('adminpanel/<str:name>/add', AddModel, name="addModel"),
    path('adminpanel/<str:name>/<int:id>', EditView, name="edit"),
    path('adminpanel/<str:name>/<int:id>/delete', DeleteModel, name="deletemodel"),
    path('adminpanel/<str:name>', ModeLlist, name="modellist"),

    
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)