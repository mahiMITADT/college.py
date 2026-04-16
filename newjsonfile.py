import json

data = {
    "name": "Lakshya",
    "age": 19,
    "city": "Pune"
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("JSON file created successfully")
