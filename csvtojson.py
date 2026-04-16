import pandas
data = pandas.read_json("employees.json")
data.to_csv("out.csv", index=False)
