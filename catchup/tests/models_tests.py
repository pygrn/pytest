from datetime import timedelta

import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from faker import Faker
from freezegun import freeze_time

from catchup.models import Event
from catchup.tests.factories import EventFactory

pytestmark = pytest.mark.django_db()
fake = Faker()


# TODO: hypothesis

@pytest.mark.xfail
def test_event_datetime():
    past_datetime = fake.date_time_between(start_date="-30y", end_date="now", tzinfo=timezone.utc)

    # No new Events with date on the past
    with pytest.raises(ValidationError):
        new_event: Event = EventFactory.create(event_datetime=past_datetime)

    # Ok to modify past Events in the future (modify description, ...)
    new_event: Event = EventFactory.create()
    with freeze_time(new_event.event_datetime + timedelta(days=1)):
        new_event.save()


def test_event_limits():
    new_event: Event = EventFactory.create()
    new_event.max_attendees = -2

    with pytest.raises(ValidationError):
        new_event.save()


def test_event_model(attendee_various):
    assert attendee_various.event is not None
