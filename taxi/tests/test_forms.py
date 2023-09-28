from django.test import TestCase
from ..forms import DriverLicenseUpdateForm, DriverCreationForm


class DriverLicenseUpdateFormTest(TestCase):
    def test_invalid_length_license_number(self) -> None:
        form = DriverLicenseUpdateForm(data={"license_number": "ABC123456"})
        self.assertFalse(form.is_valid())

    def test_invalid_upper_letters_quantity(self) -> None:
        form = DriverLicenseUpdateForm(data={"license_number": "ABCD1234"})
        self.assertFalse(form.is_valid())

    def test_invalid_digits_quantity(self) -> None:
        form = DriverLicenseUpdateForm(data={"license_number": "ABCD123"})
        self.assertFalse(form.is_valid())

    def test_valid_form(self) -> None:
        form_data = {"license_number": "ABC12345"}
        form = DriverLicenseUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class DriverCreationFormTest(TestCase):
    def test_driver_creation_form_with_license_number_is_valid(self) -> None:
        form_data = {
            "username": "test_user",
            "license_number": "ABC12345",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "password1": "test_password",
            "password2": "test_password",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
