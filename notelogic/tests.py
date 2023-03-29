from django.test import TestCase

# Create your tests here.

# This is the test for the routes
class RoutesTest(TestCase):
    def test_routes(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

# This is the test for the notes list
class NotesListTest(TestCase):
    def test_notes_list(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, 200)

# This is the test for the note detail
class NoteDetailTest(TestCase):
    def test_note_detail(self):
        response = self.client.get('/api/notes/1/')
        self.assertEqual(response.status_code, 200)

# This is the test for the note creation
class NoteCreationTest(TestCase):
    def test_note_creation(self):
        response = self.client.post('/api/notes/', {'body': 'This is a test note'})
        self.assertEqual(response.status_code, 200)

# This is the test for the note update
class NoteUpdateTest(TestCase):
    def test_note_update(self):
        response = self.client.put('/api/notes/1/', {'body': 'This is a test note'})
        self.assertEqual(response.status_code, 200)


# This is the test for the note deletion
class NoteDeletionTest(TestCase):
    def test_note_deletion(self):
        response = self.client.delete('/api/notes/1/')
        self.assertEqual(response.status_code, 200)
