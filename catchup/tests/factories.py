import random

from django.utils import timezone
import factory
from factory import DjangoModelFactory, Faker

from catchup.models import Attendee, Event, EventPhoto, Group, User

"""
# https://factoryboy.readthedocs.io/en/latest/
# https://faker.readthedocs.io/en/master/
"""


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = Faker("sentence", locale="es_ES", nb_words=4, variable_nb_words=True, ext_word_list=None)


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    group = factory.SubFactory(GroupFactory)
    name = Faker("sentence", locale="es_ES", nb_words=4, variable_nb_words=True, ext_word_list=None)
    event_datetime = Faker("future_datetime", tzinfo=timezone.utc)
    place = Faker("address")
    max_attendees = random.randint(0, 100)

    # https://factoryboy.readthedocs.io/en/stable/recipes.html?highlight=manytomanyfield
    @factory.post_generation
    def attendees(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of attendees were passed in, use them
            for attendee in extracted:
                self.attendees.add(attendee)


class AttendeeFactory(DjangoModelFactory):
    class Meta:
        model = Attendee

    event = factory.SubFactory(EventFactory)
    user = factory.SubFactory(UserFactory)
    will_attend = Faker("boolean", chance_of_getting_true=50)


class EventPhotoFactory(DjangoModelFactory):
    class Meta:
        model = EventPhoto

    photo_date = Faker("date_this_year", before_today=True)
    description = Faker("sentence", locale="es_ES", nb_words=4, variable_nb_words=True, ext_word_list=None)
