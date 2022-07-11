import asyncio
from quart import Quart, jsonify
import httpx

app = Quart(__name__)


@app.route("/recipes/<recipe_id>")
async def recipe_diagnostics(recipe_id):
    backend = "http://backend-service"
    async with httpx.AsyncClient() as client:
        recipe_crawled, recipe_indexed, recipe_history = await asyncio.gather(
            client.get(f"{backend}/recipes/{recipe_id}/crawl"),
            client.get(f"{backend}/recipes/{recipe_id}"),
            client.get(f"{backend}/recipes/{recipe_id}/history"),
        )
        return jsonify(
            {
                "crawled": recipe_crawled.json(),
                "indexed": recipe_indexed.json(),
                "history": recipe_history.json(),
            }
        )
