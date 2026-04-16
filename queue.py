class Queue:
    def __init__(self):
        self.items = []   # initialize empty queue

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, x):
        self.items.append(x)
        print(x, "inserted")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
        else:
            print("Removed:", self.items.pop(0))

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front element:", self.items[0])

    def display(self):
        if self.is_empty():
            print("Queue empty")
        else:
            print("Queue elements:", self.items)


# main program
q = Queue()

while True:
    print("\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        val = int(input("Enter value: "))
        q.enqueue(val)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.peek()
    elif ch == 4:
        q.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
