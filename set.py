# Program: Set operations

def set_demo():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}

    print("Set 1:", s1)
    print("Set 2:", s2)

    # Iteration
    print("Elements in Set 1:")
    for val in s1:
        print(val, end=" ")
    print("\n")

    # Membership
    print("Is 3 present?", 3 in s1)

    # Operations
    print("Union:", s1 | s2)
    print("Intersection:", s1 & s2)
    print("Difference (s1 - s2):", s1 - s2)
    print("Difference (s2 - s1):", s2 - s1)

set_demo()
