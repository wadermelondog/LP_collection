import csv


def load_collection(filename, create_empty=False):
    """Function to load the collection from a .csv file

    Args:
        filename (string): filename from which to load the collection

    Returns:
        list: Collection as a list of dictionaries, or an empty list
    """
    collection = []
    try:
        with open(f'{filename}', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            collection = [row for row in reader]
        print(f"Collection loaded from {filename}")
    except FileNotFoundError:
        if create_empty:
            print("Filename not found, starting with an empty collection")
            return collection
        else:
            print(f"Incorrect filename, please try again")
    return collection

#def save_collection(filename, collection):









def main():
    while True:
        print("Welcome to LP-collection, an offline tool for managing your vinyl collection!")
        while True:    
            try:
                choice = int(input("Load an existing collection(1) or make a new one(2)?: "))
            except ValueError:
                print("Incorrect number try again")
                continue
            if choice == 1:
                