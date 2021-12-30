from unittest import TestCase
from django.core import mail
from django.test import Client
from unittest.mock import patch
import pytest


# class EmailUnitTest(TestCase):
#     def test_send_email_should_succeed(self):
#         with self.settings(
#             EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
#         ):
#             self.assertEqual(len(mail.outbox), 0)

#             mail.send_mail(
#                 subject="New company added",
#                 message="Test message",
#                 from_email="test@test.com",
#                 recipient_list=["test2@test.com"],
#                 fail_silently=False,
#             )

#             self.assertEqual(len(mail.outbox), 1)

#             self.assertEqual(mail.outbox[0].subject, "New company added")

#     # def test_send_email_without_arguments_should_send_empty_email(self):
#     #     client = Client()

#     #     with patch(
#     #         "companies.views.send_mail",
#     #     ) as mock_send_mail:
#     #         res = client.post(path="/send-email")
#     #         res_content = res.json()
#     #         self.assertEqual(res.status_code, 200)
#     #         self.assertEqual(res_content.get("status"), "success")
#     #         self.assertEqual(res_content.get("message"), "Email sent")
#     #         mock_send_mail.assert_called_once_with(
#     #             subject=None,
#     #             message=None,
#     #             from_email="test@test.com",
#     #             recipient_list=["test2@test.com"],
#     #         )

#     def test_send_email_with_get_verb_should_fail(self):
#         client = Client()
#         res = client.get(path="/send-email")
#         assert res.status_code == 405
#         assert res.json() == {'detail': 'Method "GET" not allowed.'}


def test_send_email_should_succeed(mailoutbox, settings):
    settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
    assert len(mailoutbox) == 0

    mail.send_mail(
        subject="New company added",
        message="Test message",
        from_email="test@test.com",
        recipient_list=["test2@test.com"],
        fail_silently=False,
    )

    assert len(mailoutbox) == 1

    assert mailoutbox[0].subject == "New company added"
    
# def test_send_email_without_arguments_should_send_empty_email(client):
#     with patch(
#         "companies.views.send_mail",
#     ) as mock_send_mail:
#         res = client.post(path="/send-email")
#         res_content = res.json()
#         assert res.status_code == 200
#         assert res_content.get("status") == "success"
#         assert res_content.get("message") == "Email sent"
#         mock_send_mail.assert_called_once_with(
#             subject=None,
#             message=None,
#             from_email="test@test.com",
#             recipient_list=["test2@test.com"],
#         )

def test_send_email_with_get_verb_should_fail(client):
    res = client.get(path="/send-email")
    assert res.status_code == 405
    assert res.json() == {'detail': 'Method "GET" not allowed.'}
