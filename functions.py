def menu():
    print(f"Welcome to your offline vinyl collection, please choose a function.")
    print(f"1. Search \n 2. New addition \n 3. Change filename")
    choice = int(input("Choice: "))
    return choice
def loadcsv(filename):
    import csv
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        csv_read = csv.DictReader(csvfile)
        lp_list = []
        for row in csv_read:
            lp_list.append(row)
    return lp_list
def search(lplist):
    print("Insert search criteria: {lplist.keys} ")