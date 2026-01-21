from django.db import models
from django.contrib.auth.models import User

class Advocate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='advocate')
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    education = models.TextField()
    bio = models.TextField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Advocate"
        verbose_name_plural = "Advocates"


class Case(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('REJECTED', 'Rejected'),
        ('CANCELLED', 'Cancelled'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_cases')
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE, related_name='advocate_cases')
    title = models.CharField(max_length=200)
    description = models.TextField()
    case_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.client.first_name} {self.client.last_name}"

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"
        ordering = ['-created_at']
