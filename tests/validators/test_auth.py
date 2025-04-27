import pytest

from app.exceptions.auth_exceptions import InvalidEmailError
from app.utils.validators import AuthValidators


# Pruebas para validate_email
def test_validate_email_valid():
    assert AuthValidators.validate_email("test@miempresa.com") == "test@miempresa.com"  # El email es una cadena válida


def test_validate_email_domain_invalid():
    with pytest.raises(InvalidEmailError):
        AuthValidators.validate_email("test@miempresa")  # El email no tiene un dominio valido


def test_validate_email_without_at_sing():
    with pytest.raises(InvalidEmailError):
        AuthValidators.validate_email("test.com")  # El email no tiene un dominio valido


def test_validate_email_without_domain():
    with pytest.raises(InvalidEmailError):
        AuthValidators.validate_email("test")  # El email no tiene un dominio valido


def test_validate_email_at_sing_invalid():
    with pytest.raises(InvalidEmailError):
        AuthValidators.validate_email("test@.com")  # El email no tiene un dominio valido
