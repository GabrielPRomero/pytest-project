from unittest import TestCase
from django.test import Client
from django.urls import reverse
import json
import pytest
from companies.models import Company



def raise_covid19_exception():
    raise ValueError("CoronaVirus Exception")


@pytest.mark.django_db
class BasicCompanyApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.companies_url = reverse('companies-list')

    def tearDown(self):
        pass


class TestGetCompanies(BasicCompanyApiTestCase):

    def test_zero_companies_should_return_empty_list(self):
        res = self.client.get(self.companies_url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [])

    def test_one_company_exists_should_succeed(self):
        test_company = Company.objects.create(name='Amazon')
        res = self.client.get(self.companies_url)
        res_content = res.json()[0]
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_content.get("name"), test_company.name)
        self.assertEqual(res_content.get("status"), "hiring")
        self.assertEqual(res_content.get("application_link"), None)

        test_company.delete()


class TestPostCompanies(BasicCompanyApiTestCase):
    def test_create_company_without_arguments_should_fail(self):
        res = self.client.post(path=self.companies_url)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json(), {"name": ["This field is required."]})

    def test_create_exist_company_should_fail(self):
        Company.objects.create(name='Apple')
        res = self.client.post(path=self.companies_url, data={"name": "Apple"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            res.json(), {"name": ["company with this name already exists."]})

    def test_create_company_with_only_name_all_other_fields_should_be_default(self):
        res = self.client.post(path=self.companies_url,
                               data={"name": "Test Company"})
        self.assertEqual(res.status_code, 201)
        res_content = res.json()
        self.assertEqual(res_content.get("name"), "Test Company")
        self.assertEqual(res_content.get("status"), "hiring")
        self.assertEqual(res_content.get("application_link"), None)

    def test_create_company_with_layoffs_status_should_succeed(self):
        res = self.client.post(path=self.companies_url, data={
                               "name": "Test Company", "status": "layoffs"})
        self.assertEqual(res.status_code, 201)
        res_content = res.json()
        self.assertEqual(res_content.get("status"), "layoffs")

    def test_create_company_with_wrong_status_should_fail(self):
        res = self.client.post(path=self.companies_url, data={
                               "name": "Test Company", "status": "wrong_status"})
        res_content = res.json()
        self.assertEqual(res.status_code, 400)
        self.assertIn('"wrong_status" is not a valid choice.',
                      str(res_content))

    @pytest.mark.xfail
    def test_should_be_ok_if_fails(self):
        self.assertEqual(1, 2)

    @pytest.mark.skip
    def test_should_be_skipped(self):
        self.assertEqual(1, 2)

    def test_raise_covid19_exception_should_pass(self):
        with pytest.raises(ValueError) as e:
            raise_covid19_exception()
        assert "CoronaVirus Exception" == str(e.value)

import logging

logger = logging.getLogger('CORONA_LOGS')


def function_that_logs_something():
    try:
        raise ValueError("CoronaVirus Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")
        
def test_logged_warning_level(caplog):
        function_that_logs_something()
        assert "I am logging CoronaVirus Exception" in caplog.text

def test_logged_info_level(caplog):
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text
