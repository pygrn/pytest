from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .admin_mixins import NoInlinesOnAddMixin
from .models import Attendee, Event, EventPhoto, Group, Profile

User = get_user_model()


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'will_attend')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class EventPhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 0


class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 0


@admin.register(Event)
class EventAdmin(NoInlinesOnAddMixin, admin.ModelAdmin):
    list_display = ('group', 'event_datetime', 'place', 'max_attendees')
    search_fields = ('group',)
    inlines = (AttendeeInline, EventPhotoInline,)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(NoInlinesOnAddMixin, BaseUserAdmin):
    inlines = (ProfileInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
