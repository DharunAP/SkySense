from django.core.management.base import BaseCommand
from whatsapp_bot.tasks import start_scheduler

class Command(BaseCommand):
    help = 'Starts the scheduler'

    def handle(self, *args, **options):
        start_scheduler()