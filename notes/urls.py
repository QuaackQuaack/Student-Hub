from django.urls import path

from .views import NotesHomePageView, NotesPageView, NotesEditView, NotesDeleteView, NotesNewView

urlpatterns = [
        path("noteshome", NotesHomePageView.as_view(), name = 'noteshome'), 
        path("<int:pk>", NotesPageView.as_view(),  name = 'noteslist'),
        path("<int:pk>/edit", NotesEditView.as_view(), name = 'notesedit'),
        path("<int:pk>/delete", NotesDeleteView.as_view(), name = 'notesdelete'),
        path("new/", NotesNewView.as_view(), name = 'notesnew'), 
        ]
