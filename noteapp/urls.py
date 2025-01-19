from django.urls import path
from .import views

urlpatterns = [
    path('notes/',views.notes, name="notes"),
    path('notes/<slug:slug>/',views.note_detial, name="note-detail"),
    path('notes-search/',views.search_notes, name="search-notes"),
]


# endpoint
# GET_ALL_NOTES_AND_CREATE_NEW_NOTE = "http://127.0.0.1:8000/notes/"
# GET_SPECIFIC_NOTE = "http://127.0.0.1:8000/notes/note-slug"
# Search-Notes= http://127.0.0.1:8000/notes-search/?search=dj