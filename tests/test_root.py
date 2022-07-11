import pytest


@pytest.mark.respx(base_url="http://backend-service", assert_all_called=True)
async def test_request(client, respx_mock):
    recipe_id = "example_id"
    recipe = {"id": recipe_id}

    respx_mock.get(f"/recipes/{recipe_id}/crawl").respond(json=recipe)
    respx_mock.get(f"/recipes/{recipe_id}").respond(json=recipe)
    respx_mock.get(f"/recipes/{recipe_id}/history").respond(json=recipe)

    data = await client.get(f"/recipes/{recipe_id}")
    data = await data.json

    assert data == {
        "crawled": recipe,
        "indexed": recipe,
        "history": recipe,
    }
