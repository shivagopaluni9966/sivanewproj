from flask import Flask, render_template, abort
import json

app = Flask(__name__)

def load_items():
    """Load Pixell.AI data from app.json"""
    with open('app.json', encoding='utf-8') as f:
        return json.load(f)

items = load_items()

@app.route('/')
def index():
    # Separate by category for easier rendering in templates
    productions = [i for i in items if i["category"] == "Production"]
    services = [i for i in items if i["category"] == "Service"]
    stories = [i for i in items if i["category"] == "Stories"]

    return render_template(
        'index.html',
        productions=productions,
        services=services,
        stories=stories
    )

@app.route('/item/<int:item_id>')
def item_detail(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        abort(404)
    return render_template('detail.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)

