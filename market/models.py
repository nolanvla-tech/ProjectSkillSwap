from django.conf import settings
from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('tutoring', 'Tutoring'),
        ('design', 'Design'),
        ('coding', 'Coding'),
        ('other', 'Other'),
    ]

    CONTACT_CHOICES = [
        ('email', 'Email'),
        ('chat', 'Chat / DM'),
        ('phone', 'Phone'),
    ]

    AVAILABILITY_CHOICES = [
        ('open', 'Open'),
        ('busy', 'Busy'),
        ('away', 'Away'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Leave blank if the skill is free.',
    )
    is_free = models.BooleanField(default=False)
    contact_preference = models.CharField(max_length=20, choices=CONTACT_CHOICES)
    availability_status = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='open',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='skills',
    )

    def __str__(self):
        return f'{self.title} by {self.owner.username}'

    def display_price(self):
        if self.is_free:
            return 'Free'
        if self.price is None:
            return 'Contact for price'
        return f'${self.price:.2f}'
