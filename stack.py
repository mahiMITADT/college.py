class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, x):
        self.items.append(x)
        print(x, "pushed")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            print("Popped:", self.items.pop())

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.items[-1])

    def display(self):
        if self.is_empty():
            print("Stack empty")
        else:
            print("Stack elements:", self.items)


s = Stack()

while True:
    print("\n1.Push 2.Pop 3.Peek 4.Display 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        val = int(input("Enter value: "))
        s.push(val)
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.peek()
    elif ch == 4:
        s.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
