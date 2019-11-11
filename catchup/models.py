from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Attendee(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    will_attend = models.BooleanField(default=False)


class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    event_date = models.DateField(null=True, blank=True)
    event_time = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=100, null=False, blank=True)
    max_attendees = models.IntegerField(default=0, help_text='0 = unlimited')
    attendees = models.ManyToManyField(User, through=Attendee)

    def __str__(self):
        return '{group}: {name} @ {event_date}'.format(
            group=self.group,
            name=self.name,
            event_date=self.event_date
        )


class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField()
    photo_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=100, null=False, blank=True)
