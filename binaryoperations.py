import pickle

class PickleHandler:
    def __init__(self, filename):
        self.filename = filename   # initialize file name

    # -------- WRITE DATA --------
    def write_data(self):
        n = int(input("How many records? "))
        data_list = []

        for i in range(n):
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
            data_list.append({"name": name, "marks": marks})

        with open(self.filename, "wb") as f:
            pickle.dump(data_list, f)

        print("Data stored successfully")

    # -------- READ DATA --------
    def read_data(self):
        try:
            with open(self.filename, "rb") as f:
                data = pickle.load(f)
                print("\nStored Records:")
                for d in data:
                    print(d)
        except:
            print("File not found")

    # -------- SEARCH RECORD --------
    def search(self):
        try:
            with open(self.filename, "rb") as f:
                data = pickle.load(f)

            key = input("Enter name to search: ")
            found = False

            for d in data:
                if d["name"] == key:
                    print("Record Found:", d)
                    found = True

            if not found:
                print("Record not found")

        except:
            print("File not found")

    # -------- STORE IMAGE --------
    def store_image(self):
        try:
            with open("image.jpeg", "rb") as img:
                img_data = img.read()

            with open("image.dat", "wb") as f:
                pickle.dump(img_data, f)

            print("Image stored successfully")

        except:
            print("Image file not found")


# -------- MAIN MENU --------
p = PickleHandler("student.dat")

while True:
    print("\n--- PICKLE MENU ---")
    print("1. Write Records")
    print("2. Read Records")
    print("3. Search Record")
    print("4. Store Image")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        p.write_data()
    elif ch == 2:
        p.read_data()
    elif ch == 3:
        p.search()
    elif ch == 4:
        p.store_image()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
