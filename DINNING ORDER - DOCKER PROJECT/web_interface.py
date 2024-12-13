# Student Name 2024-2026: Pooja Ravikumar
# ASU ID: 1234370880
# Date: 30/11/2024

from flask import Flask, render_template, redirect, url_for



# Simulate kitchen resources
Hardware_resources = {
    "Oven": "Available",
    "Stove": "Available",
    "Mixer": "Available",
    "Knife": "Available"
}
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", resources=Hardware_resources)

@app.route("/request/<tool>", methods=['GET'])
def request_resource_web(tool):
    # Check the current status of the resource and toggle it
    if Hardware_resources.get(tool) == "Available":
        Hardware_resources[tool] = "Occupied"
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
