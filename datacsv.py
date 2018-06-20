from csv import reader


with open("fighters.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        #each row is a list!
        print(row)


