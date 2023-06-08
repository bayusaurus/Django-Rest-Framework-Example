from django.db import models

STATUS_CHOICHES = [
    ('Publish', 'Publish'),
    ('Draft', 'Draft'),
    ('Trash', 'Trash'),
]


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100,  choices=STATUS_CHOICHES, default='Draft')
    
    def __str__(self):
        return self.title