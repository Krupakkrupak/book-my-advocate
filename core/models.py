from django.db import models

class Advocate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Case(models.Model):
    STATUS_CHOICES = [
        ('won', 'Won'),
        ('lost', 'Lost'),
        ('ongoing', 'Ongoing'),
    ]

    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE, related_name='cases')
    client_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.advocate.name})"

