def test_request(client):
    client.get("/recipes/example_id")
