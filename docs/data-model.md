Model de dades Catch Up (Meetup)

User
- username (email)
- name
- is_premium

Group
- name
- members (User list)

Attendee
- Event
- User
- will_attend

Event
- Group
- name
- date
- time
- place
- max_attendees
- attendees (Attendee list)

EventPhoto
- Event
- image
- date
- description
