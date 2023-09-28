# Testing server json output
# You can use these following links with Postman to test the API

import requests

response = requests.get("http://127.0.0.1:8000/").json()
print(response)
print()

# Add new item
print("Adding an Item:")
addItem = requests.post(
    "http://127.0.0.1:8000/",
    json={
        "name": "Hammer",
        "price": 20.0,
        "count": 5,
        "id": 5,
        "category": "tools",
    },
).json()
print(addItem)

# Check the updates
response = requests.get("http://127.0.0.1:8000/").json()
print(response)
print()

# Update an item
print("Updating an item:")
updateItem = requests.put(
    "http://127.0.0.1:8000/update/1?count=50").json()
print(updateItem)

# Check the updates
response = requests.get("http://127.0.0.1:8000/").json()
print(response)
print()


# Delete an item
print("Deleting an item:")
deleteItem = requests.delete("http://127.0.0.1:8000/delete/0").json()

print(deleteItem)

# Check the updates
response = requests.get("http://127.0.0.1:8000/").json()
print(response)
print()
