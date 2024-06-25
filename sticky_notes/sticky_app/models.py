from django.db import models

class StickyNote(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    


    def __str__(self):
        return self.title or self.content[:20]  # Display title if available, else truncate content
