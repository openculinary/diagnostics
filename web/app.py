from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/recipes/<recipe_id>')
def recipe_diagnostics(recipe_id):
    backend = 'http://backend-service'
    recipe_crawled = requests.get(f'{backend}/recipes/{recipe_id}/crawl')
    recipe_indexed = requests.get(f'{backend}/recipes/{recipe_id}')
    recipe_history = requests.get(f'{backend}/recipes/{recipe_id}/history')
    return jsonify({
        'crawled': recipe_crawled.json(),
        'indexed': recipe_indexed.json(),
        'history': recipe_history.json(),
    })
