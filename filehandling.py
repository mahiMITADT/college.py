class FileHandler:
    def __init__(self, filename):
        self.filename = filename   # file name initialize

    def write_file(self):
        with open(self.filename, "w") as f:
            data = input("Enter text: ")
            f.write(data)
        print("Data written successfully")

    def read_file(self):
        try:
            with open(self.filename, "r") as f:
                print("\nFile Content:")
                print(f.read())
        except:
            print("File not found")

    def append_file(self):
        with open(self.filename, "a") as f:
            data = input("Enter text to append: ")
            f.write("\n" + data)
        print("Data appended successfully")

    def count_words(self):
        try:
            with open(self.filename, "r") as f:
                data = f.read()
                words = data.split()
                print("Total words:", len(words))
        except:
            print("File not found")


# main program
file = FileHandler("data.txt")

while True:
    print("\n--- FILE MENU ---")
    print("1. Write")
    print("2. Read")
    print("3. Append")
    print("4. Count Words")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        file.write_file()
    elif ch == 2:
        file.read_file()
    elif ch == 3:
        file.append_file()
    elif ch == 4:
        file.count_words()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
