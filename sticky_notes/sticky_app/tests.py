from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import StickyNote 
# Create your tests here.

class StickNoteModelTest(TestCase):
    def setUp(self) -> None:
        #Create a StickyNote object
        sticky_note = StickyNote.objects.create(title ='Test Sticky Note'
                                                ,content='This is a test note.')
                                                
    def test_note_has_title(self):
        #Test that Sticky Note has correct title
        note = StickyNote.objects.get(id=1)
        self.assertEqual(note.title,'Test Sticky Note')

    def test_note_has_content(self):
        # Test that Stick Note has correct content
        note = StickyNote.objects.get(id=1)
        self.assertEqual(note.content,'This is a test note.')

    def test_note_published_date(self):
        # Test that timestamps are correct
        note = StickyNote.objects.get(id=1)
        now = timezone.now()
        self.assertAlmostEqual(note.published_date, now, 
                               delta=timezone.timedelta(seconds=1))


class StickyNoteViewTests(TestCase):

    def setUp(self):
        # Create a StickyNote instance to use in the tests
        self.note = StickyNote.objects.create(title="Note 1", content="Content 1")

    def test_index_view(self):
        # Simulate a GET request to the index view
        response = self.client.get(reverse('index'))
        # Verify the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'sticky_app/index.html')
        # Verify the response contains the title of the created note
        self.assertContains(response, self.note.title)

    def test_add_note_view_get(self):
        # Simulate a GET request to the add note view
        response = self.client.get(reverse('add_note'))
        # Verify the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'sticky_app/add_note.html')

    def test_add_note_view_post(self):
        # Simulate a POST request to add a new note
        response = self.client.post(reverse('add_note'), {'title': 'Note 2', 'content': 'Content 2'})
        # Verify the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # Ensure the view redirects to the index
        self.assertRedirects(response, reverse('index'))
        # Check that the new note is created in the database
        self.assertTrue(StickyNote.objects.filter(title='Note 2', content='Content 2').exists())

    def test_view_note_view(self):
        # Simulate a GET request to view a specific note
        response = self.client.get(reverse('view_note', args=[self.note.id]))
        # Verify the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'sticky_app/view_note.html')
        # Verify the response contains the note's title and content
        self.assertContains(response, self.note.title)
        self.assertContains(response, self.note.content)

    def test_edit_note_view_get(self):
        # Simulate a GET request to the edit note view
        response = self.client.get(reverse('edit_note', args=[self.note.id]))
        # Verify the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'sticky_app/edit_note.html')
        # Verify the response contains the current note's title and content
        self.assertContains(response, self.note.title)
        self.assertContains(response, self.note.content)

    def test_edit_note_view_post(self):
        # Simulate a POST request to update a note
        response = self.client.post(reverse('edit_note', args=[self.note.id]), {'title': 'Updated Title', 'content': 'Updated Content'})
        # Verify the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # Ensure the view redirects to the view note page
        self.assertRedirects(response, reverse('view_note', args=[self.note.id]))
        # Refresh the note instance from the database to get the updated data
        self.note.refresh_from_db()
        # Verify the note's title and content are updated
        self.assertEqual(self.note.title, 'Updated Title')
        self.assertEqual(self.note.content, 'Updated Content')

    def test_delete_note_view(self):
        # Simulate a POST request to delete a note
        response = self.client.post(reverse('delete_note', args=[self.note.id]))
        # Verify the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # Ensure the view redirects to the index
        self.assertRedirects(response, reverse('index'))
        # Check that the note is deleted from the database
        self.assertFalse(StickyNote.objects.filter(id=self.note.id).exists())
