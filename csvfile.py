import csv

with open("stud.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["id","name"])

    for i in range(2):
        w.writerow([i, input("Name:")])
