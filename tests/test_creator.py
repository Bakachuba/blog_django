import pytest
from app.models import Creator


@pytest.mark.django_db
def test_creator_str():
    creator = Creator.objects.create(full_name="Alice")
    assert str(creator) == "Alice"


@pytest.mark.django_db
def test_creator_post_count(api_client):
    response = api_client.post('/api/creators/', {"full_name": "Bob"}, format='json')
    assert response.status_code == 201
    data = response.json()
    assert data["post_count"] == 0
