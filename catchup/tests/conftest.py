import pytest

from catchup.models import Attendee
from catchup.tests.factories import AttendeeFactory


@pytest.fixture
def attendee(db) -> Attendee:
    attendee = AttendeeFactory()
    yield attendee
    attendee.delete()


@pytest.fixture(
    scope="function",
    params=[
        ["Attendee will attend", True],
        ["Attendee will not attend", False],
    ])
def attendee_various(request) -> Attendee:
    req_attendee_name = request.param[0]
    req_attendee_attend = request.param[1]

    # Returns a User instance that's not saved
    # AttendeeFactory.build()
    # Returns a saved User instance
    # AttendeeFactory.create()
    # Returns a stub object (just a bunch of attributes)
    # AttendeeFactory.stub()

    new_attendee: Attendee = AttendeeFactory.create()
    new_attendee.will_attend = req_attendee_attend
    new_attendee.save()

    yield new_attendee
    new_attendee.delete()
