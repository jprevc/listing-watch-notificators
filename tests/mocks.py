"""
Mock HTTPS sessions and SMTP connections, which record what the Notificators send.
"""

import requests

# pylint: disable=unused-argument


class HttpsSessionMock:
    """
    HTTPS Session mock class.
    """

    def __init__(self):
        self.simulated_messages = []

    def post(self, url, data, headers):
        self.simulated_messages.append(data["message"])


class NtfySessionMock:
    """
    HTTPS Session mock class for the ntfy notificator, whose 'post' call shape (raw bytes body,
    headers carrying title/priority/tags/click/auth info) differs from Pushover's form-encoded dict.
    """

    def __init__(self, status_code=200):
        self.simulated_messages = []
        self.simulated_headers = []
        self.simulated_urls = []
        self.simulated_auth = []
        self.status_code = status_code

    def post(self, url, data=None, headers=None, auth=None) -> requests.Response:
        self.simulated_urls.append(url)
        self.simulated_messages.append(data.decode("utf-8") if isinstance(data, (bytes, bytearray)) else data)
        self.simulated_headers.append(headers or {})
        self.simulated_auth.append(auth)
        response = requests.Response()
        response.status_code = self.status_code
        return response


class SmtpMock:
    """
    SMTP mock class
    """

    def __init__(self):
        self.simulated_messages = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def ehlo(self):
        pass

    def starttls(self):
        pass

    def login(self, user, password):
        pass

    def sendmail(self, user, recipients, message):
        self.simulated_messages.append(message)
