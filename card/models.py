from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail


class Card(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Card)
def send_card_added_email_(sender, instance, **kwargs):
    try:
        send_mail(
            'Card added',
            f"{instance.name} has been added to the card",
            'from@example.com',
            ['to@example.com'],
            fail_silently=False
        )
    except:
        print("smtp servers are not configured")
