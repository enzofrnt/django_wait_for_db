import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from django.db import DEFAULT_DB_ALIAS
from django.conf import settings


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write("Waiting for database...")
        self.stdout.flush()

        db_settings = settings.DATABASES["default"]
        db_host = db_settings.get("HOST", "")
        db_port = db_settings.get("PORT", "")

        while True:
            try:
                db_conn = connections[DEFAULT_DB_ALIAS]
                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database available!"))
                self.stdout.flush()
                break
            except OperationalError:
                if db_host or db_port:
                    self.stdout.write(
                        f"Database unavailable on {db_host}:{db_port}, waiting 1 second..."
                    )
                else:
                    self.stdout.write(
                        "Database unavailable (no host/port specified), waiting 1 second..."
                    )
                self.stdout.flush()
                time.sleep(1)
