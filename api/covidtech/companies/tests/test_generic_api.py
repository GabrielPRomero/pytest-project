import responses
import requests
import json
import pytest

testing_env_url = "http://localhost:8000/companies/"


def test_zero_companies_django_agnostic():
    res = requests.get(url=testing_env_url)
    assert res.status_code == 200
    assert res.json() == []


def test_create_company_with_layoffs_django_agnostic():
    res = requests.post(url=testing_env_url, json={
        "name": "Test Company", "status": "layoffs"})
    assert res.status_code == 201
    res_content = res.json()
    assert res_content.get("status") == "layoffs"
    cleanpup_company(company_id=res_content.get("id"))

# python manage.py flush to clean db


def cleanpup_company(company_id: str):
    res = requests.delete(url=f"{testing_env_url}{company_id}/")
    assert res.status_code == 204


@pytest.mark.crypto
def test_dogecoin_api():
    res = requests.get("https://api.cryptonator.com/api/ticker/doge-usd",
                       headers={'User-Agent': 'Mozilla/5.0'})
    assert res.status_code == 200
    res_content = res.json()
    assert res_content.get("ticker").get("base") == "DOGE"
    assert res_content.get("ticker").get("target") == "USD"


# Mocking response for schema validation
@pytest.mark.crypto
@responses.activate
def test_mocked_dogecoin_api():
    responses.add(
        method=responses.GET, url="https://api.cryptonator.com/api/ticker/doge-usd",
        json={
            "ticker": {
                "base": "Test",
                "target": "Test-USD",
                "price": "0.14585899",
                "volume": "330449544.56863999",
                "change": "-0.00208463"
            },
            "timestamp": 1640860742,
            "success": True,
            "error": ""
        },
        status=200
    )

    res = requests.get("https://api.cryptonator.com/api/ticker/doge-usd",
                       headers={'User-Agent': 'Mozilla/5.0'})

    assert res.status_code == 200
    res_content = res.json()
    assert res_content.get("ticker").get("base") == "Test"
    assert res_content.get("ticker").get("target") == "Test-USD"
