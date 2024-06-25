from django.urls import path
from .import views

# URL patterns for the sticky_app application
urlpatterns = [
            path('', views.index, name='index'),
            path('add/', views.add_note, name='add_note'),
            path('post/<int:note_id>/', views.view_note, name='view_note'),
            path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
            path('note/<int:note_id>/delete/', views.delete_note, name='delete_note'),

]