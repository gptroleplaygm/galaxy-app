from flask import Flask, request, jsonify

app = Flask(__name__)

# Test route to make sure app is running
@app.get("/")
def hello():
    return {"message": "Galaxy of Consequence online."}

# In-memory character store
characters = {}

# Save a character
@app.post("/character")
def create_character():
    data = request.json
    characters[data["id"]] = data
    return {"ok": True, "character": data}

# Get a character by ID
@app.get("/character/<char_id>")
def get_character(char_id):
    char = characters.get(char_id)
    if not char:
        return {"ok": False, "error": "Not found"}, 404
    return {"ok": True, "character": char}

if __name__ == "__main__":
    app.run(debug=True)
