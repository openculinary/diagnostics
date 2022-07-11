from flask import Flask, jsonify
from requests_futures.sessions import FuturesSession

app = Flask(__name__)


@app.route("/recipes/<recipe_id>")
def recipe_diagnostics(recipe_id):
    backend = "http://backend-service"
    session = FuturesSession()
    recipe_crawled = session.get(f"{backend}/recipes/{recipe_id}/crawl")
    recipe_indexed = session.get(f"{backend}/recipes/{recipe_id}")
    recipe_history = session.get(f"{backend}/recipes/{recipe_id}/history")
    return jsonify(
        {
            "crawled": recipe_crawled.result().json(),
            "indexed": recipe_indexed.result().json(),
            "history": recipe_history.result().json(),
        }
    )
