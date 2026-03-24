# Program: Tuple operations

def tuple_demo():
    t = (10, 20, 30, 40, 50)
    print("Tuple:", t)

    # Access
    print("First:", t[0])
    print("Last:", t[-1])
    print("Slice:", t[1:4])

    # Nested tuple
    nested = ("Python", (1, 2, 3), ["a", "b"])
    print("Nested:", nested)

    print("From inner tuple:", nested[1][1])
    print("From list:", nested[2][0])

    # Repetition
    t2 = ("Hi", "Bye")
    print("Repeated:", t2 * 3)

tuple_demo()
