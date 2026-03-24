# Program: Basic operations on Lists

def list_demo():
    nums = [10, 20, 30, 40, 50]
    print("Initial List:", nums)

    # Access elements
    print("First:", nums[0])
    print("Last:", nums[-1])
    print("Slice (1 to 3):", nums[1:4])
    print()

    # Add elements
    nums.append(60)
    nums.insert(2, 25)
    print("After adding elements:", nums)

    # Remove elements
    removed = nums.pop()
    nums.remove(25)
    print("After removing:", nums, "| Removed:", removed)

    # Sorting
    nums.sort()
    print("Ascending:", nums)

    nums.sort(reverse=True)
    print("Descending:", nums)

    # Reverse
    nums.reverse()
    print("Reversed:", nums)

list_demo()
