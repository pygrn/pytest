import pytest

from catchup.models import Attendee, Group, Event
from catchup.tests.factories import AttendeeFactory, GroupFactory, EventFactory


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

    new_attendee: Attendee = AttendeeFactory.create()
    new_attendee.will_attend = req_attendee_attend
    new_attendee.save()

    yield new_attendee
    new_attendee.delete()


@pytest.fixture(
    params=[
        ["Group 1"],
        ["Group 2"],
    ])
def group_various(request) -> Group:
    req_group_name = request.param[0]

    new_group: Group = GroupFactory.create(name=req_group_name)
    new_group.save()

    yield new_group
    new_group.delete()


@pytest.fixture(
    params=[
        ["Event 1", "Girona", 200],
        ["Event 2", "Barcelona", 0],
        ["Event 3", "Tarragona", 0],
    ])
def event_various(request, group_various) -> Event:
    req_event_name = request.param[0]
    req_event_place = request.param[1]
    req_event_max_attendees = request.param[2]

    new_event: Event = EventFactory.create(name=req_event_name,
                                           max_attendees=req_event_max_attendees,
                                           place=req_event_place)
    new_event.save()

    yield new_event
    new_event.delete()
