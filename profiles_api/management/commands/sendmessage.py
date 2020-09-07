from django.core.management import BaseCommand
from django.utils import timezone
from push_notifications.models import APNSDevice

from profiles_api.models import Capsule


class Command(BaseCommand):

    def handle(self, *args, **options):
        users_query = Capsule.objects.exclude(notificationsent=True).filter(date_to_open__lte=timezone.now())


        userq = users_query.values_list('shared_to', flat=True)
        tokens_query = list(APNSDevice.objects.filter(user__in=userq).values_list('registration_id', flat=True).distinct())

        for token in tokens_query:
            device = APNSDevice.objects.get(registration_id=token)
            device.send_message(" omae wa mou shindeiru ＼(≧▽≦)／ NOLAN FELICITY MY CRUSH", sound='default')

        for gap in users_query.all():
            gap.notificationsent = True
            gap.save()