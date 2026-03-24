# Program: Dictionary operations

def dict_demo():
    data = {"name": "John", "age": 25, "city": "New York"}
    print("Original:", data)

    # Access
    print("Name:", data["name"])
    print("Age:", data.get("age"))

    # Update
    data["age"] = 26
    data["email"] = "john@mail.com"
    print("Updated:", data)

    # Remove
    removed = data.pop("city")
    print("After removal:", data)
    print("Removed value:", removed)

dict_demo()
