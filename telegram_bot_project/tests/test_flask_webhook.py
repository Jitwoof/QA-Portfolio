# test_flask_webhook.py
import sys
import os
import json
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from flask_app import app
from telegram import Update

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_webhook_valid_update(client):
    """Simulate a valid Telegram webhook POST"""
    sample_update = {
        "update_id": 123456789,
        "message": {
            "message_id": 1,
            "from": {
                "id": 1111111,
                "is_bot": False,
                "first_name": "Test",
                "username": "testuser",
                "language_code": "en"
            },
            "chat": {
                "id": 1111111,
                "first_name": "Test",
                "username": "testuser",
                "type": "private"
            },
            "date": 1690000000,
            "text": "/faq"
        }
    }

    response = client.post(
        '/WEBHOOK-SECRET', 
        data=json.dumps(sample_update),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert b'ok' in response.data
