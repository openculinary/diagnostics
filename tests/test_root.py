import responses


@responses.activate
def test_request(client):
    recipe_id = "example_id"
    recipe = {"id": recipe_id}

    responses.get(f"http://backend-service/recipes/{recipe_id}/crawl", json=recipe)
    responses.get(f"http://backend-service/recipes/{recipe_id}", json=recipe)
    responses.get(f"http://backend-service/recipes/{recipe_id}/history", json=recipe)

    data = client.get(f"/recipes/{recipe_id}").json

    assert data == {
        "crawled": recipe,
        "indexed": recipe,
        "history": recipe,
    }
