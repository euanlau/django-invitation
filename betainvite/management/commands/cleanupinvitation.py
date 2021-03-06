"""
A management command which deletes expired keys (e.g.,
keys which were never activated) from the database.

Calls ``InvitationKey.objects.delete_expired_keys()``, which
contains the actual logic for determining which keys are deleted.

"""

from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "Delete expired invitations' keys from the database"

    def handle_noargs(self, **options):
        from betainvite.models import InvitationKey
        InvitationKey.objects.delete_expired_keys()
