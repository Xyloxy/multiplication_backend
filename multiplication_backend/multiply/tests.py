from django.test import TestCase
from rest_framework.test import APIRequestFactory
from multiplication_backend.multiply.views import MultiplyView


# Not the cleanest way to create the tests, as assertions should be only done
# at the end of the test, but as this is a simple example and I don't want to overcomplicate
# it with pytest's parametrize, I just added a for loop.
class MultiplyTest(TestCase):
    def test_multiplication(self):
        factory = APIRequestFactory()

        parameters = [
            (2, 2, 4),
            (2.2, 2.4, 5.28),
            (2.1, 2, 4.2),
            (2, 2.4, 4.8),
        ]

        for number1, number2, expected in parameters:
            request = factory.post("/notes/", {"number1": number1, "number2": number2})

            response = MultiplyView.as_view()(request)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {"result": expected})

    def test_multiplication_no_data(self):
        factory = APIRequestFactory()

        request = factory.post("/notes/", {})

        response = MultiplyView.as_view()(request)

        self.assertEqual(response.status_code, 400)

    def test_multiplication_bad_data(self):
        factory = APIRequestFactory()

        parameters = [
            ("abc", "def"),
            (1, "def"),
            ("abc", 2),
        ]

        for number1, number2 in parameters:
            request = factory.post("/notes/", {"number1": number1, "number2": number2})

            response = MultiplyView.as_view()(request)

            self.assertEqual(response.status_code, 400)
