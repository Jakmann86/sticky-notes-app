from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote

# View to display all notes
def index(request):
    notes = StickyNote.objects.all()
    return render(request, 'sticky_app/index.html', {'notes':notes})

# View to add a new note
def add_note(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        title = request.POST.get('title')
        StickyNote.objects.create(content=content, title=title)
        return redirect('index')
    return render(request, 'sticky_app/add_note.html')

# View to display a specific note
def view_note(request, note_id):
    note = get_object_or_404(StickyNote, id=note_id)
    return render(request, 'sticky_app/view_note.html', context={'note':note})

# View to edit an existing note
def edit_note(request, note_id):
    note = get_object_or_404(StickyNote, pk = note_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        title = request.POST.get('title')
        note.content = content
        note.title = title
        note.save()
        return redirect('view_note', note_id=note.id)
    return render(request, 'sticky_app/edit_note.html', {'note':note})

# View to delete a note
def delete_note(request, note_id):
    note = get_object_or_404(StickyNote, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    return redirect('view_note', note_id=note_id)
