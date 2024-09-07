import pytest
from unittest.mock import patch
from django.core.management import call_command
from django.test import override_settings
from django.db.utils import OperationalError


@pytest.mark.django_db
def test_handle_successful_database_connection_with_sqlite(capfd):
    """Test the management command when the database is available"""

    with patch("django.db.connections.__getitem__") as mock_getitem:
        mock_getitem.return_value.ensure_connection.return_value = True

        call_command("wait_for_db")
        out, _ = capfd.readouterr()

        assert "Waiting for database..." in out
        assert "Database available!" in out


@pytest.mark.django_db
def test_handle_database_unavailable_then_available_with_sqlite(capfd):
    """Test the management command when the database is unavailable at first"""

    with patch(
        "django.db.backends.base.base.BaseDatabaseWrapper.ensure_connection"
    ) as mock_ensure_connection:
        mock_ensure_connection.side_effect = [
            OperationalError,
            OperationalError,
            OperationalError,
            True,
        ]

        call_command("wait_for_db")

        out, _ = capfd.readouterr()

        assert "Waiting for database..." in out
        assert (
            out.count(
                "Database unavailable (no host/port specified), waiting 1 second..."
            )
            == 3
        )
        assert "Database available!" in out


@pytest.mark.django_db
@override_settings(
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
)
def test_handle_successful_database_connection_with_postgresql(capfd):
    """Test the management command when the database is available"""

    with patch("django.db.connections.__getitem__") as mock_getitem:
        mock_getitem.return_value.ensure_connection.return_value = True

        call_command("wait_for_db")

        out, err = capfd.readouterr()

        assert "Waiting for database..." in out
        assert "Database available!" in out


@pytest.mark.django_db
@override_settings(
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
)
def test_handle_database_unavailable_then_available_with_postgresql(capfd):
    """Test the management command when the database is unavailable at first"""

    with patch(
        "django.db.backends.base.base.BaseDatabaseWrapper.ensure_connection"
    ) as mock_ensure_connection:
        mock_ensure_connection.side_effect = [
            OperationalError,
            OperationalError,
            OperationalError,
            True,
        ]

        call_command("wait_for_db")

        out, _ = capfd.readouterr()

        assert "Waiting for database..." in out
        assert out.count("Database unavailable on 127.0.0.1:5432, waiting 1 second...")
        assert "Database available!" in out
