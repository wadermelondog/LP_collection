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

def add_record(collection) -> list:
    from datetime import datetime
    """Function to add a record to the collection

    Args:
        collection (list): collection as a list of dictionaries
    Catalog#,Artist,Title,Label,Format,Rating,Released,release_id,CollectionFolder,Date Added,Collection Media Condition,Collection Sleeve Condition,Collection Notes
    Returns:
        list: Updated collection
    """
    record = {}
    while True:
        print("Enter the following fields for the record:")
        print(collection[0].keys())
        for key in collection[0].keys():
            if key == 'Date Added':
                record[key] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            else:
                record[key] = input(f"Enter {key}: ")
        collection.append(record)
        print(f"Record {record['Title']} by {record['Artist']} added to the collection")
        return collection
    
def search_collection(collection):
    """Function to search the collection

    Args:
        collection (list): collection as a list of dictionaries

    Returns:
        list: Collection as a list of dictionaries
    """
    search_key = input(f"Enter the search key {collection.keys[0]}, leave empty to search everything: ")
    search_term = input("Enter the search term: ")
    search_results = []
    for record in collection:
        if search_key == "":
            for 

