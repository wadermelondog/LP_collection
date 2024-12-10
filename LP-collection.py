import csv
from datetime import datetime

def load_collection() -> list:
    """Function to load the collection from a .csv file

    Returns:
        list: collection as list of dictionaries
        string: filename   
    """
    while True:
        collection = []
        filename = input("Enter filename to load the collection from, leave empty for default (collection.csv): ")
        if not filename:
            filename = "collection.csv"
        try:
            if filename.endswith(".csv"):
                with open(f'{filename}', mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    collection = [row for row in reader]
                print(f"Collection loaded from {filename}")
                return collection, filename
            else:
                try:
                    filename = filename + ".csv"
                    with open(f'{filename}', mode='r', newline='', encoding='utf-8') as file:
                        reader = csv.DictReader(file)
                        collection = [row for row in reader]
                    print(f"Collection loaded from {filename}")
                    return collection, filename
                except FileNotFoundError:
                    print("Invalid filename, please try again.")
                    continue
        except FileNotFoundError:
            print(f"File {filename} not found.")
            while True:
                choice = input("Would you like to create a new collection? Yes or No: ")
                if choice.lower() == "yes" or choice.lower() == "y":
                    choice = str(input("Enter the name of the new collection without .csv, or leave empty for default: "))
                    if not choice:
                        choice = "collection"
                    print(f"Creating a new collection with the filename {choice}.csv")
                    collection = []
                    filename = choice + ".csv"
                    return collection, filename
                elif choice.lower() == "no" or choice.lower() == "n":
                    print("Trying again")
                    break
                else:  
                    print("Invalid choice, trying again")
                    continue
                

def add_record(collection) -> list:
    """Function to add a record to the collection
        Checks which input type is expected for the field and asks for it.
        Asks for the condition of the record by displaying the options for it.
    Args:
        collection (list): collection as a list of dictionaries

    Returns:
        list: Updated collection
    """
    record = {}
    input_types = {
        "Catalog#": str,
        "Artist": str,
        "Title": str,
        "Label": str,
        "Format": str,
        "Rating": int,
        "Released": int,
        "release_id": str,
        "CollectionFolder": str,
        "Date Added": str,
        "Collection Media Condition": str,
        "Collection Sleeve Condition": str,
        "Collection Notes": str}
    while True:
        print("Enter the details for the record:")
        for key in input_types.keys():
            while True:
                if key == "Date Added":
                    record[key] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                elif key == "Collection Media Condition" or key == "Collection Sleeve Condition":
                    try:    
                        print(f"Choose {key}")
                        print("Choose from the following options:")
                        print("1. M, 2. NM, 3. VG+, 4. VG, 5. G+, 6. G, 7. F, 8. P")
                        conditions = {1: "M", 2: "NM", 3: "VG+", 4: "VG", 5: "G+", 6: "G", 7: "F", 8: "P"}
                        condition = int(input("Enter the choice: "))
                        if condition not in conditions:
                            print("Invalid choice, try again.")
                            continue
                        record[key] = conditions[condition]
                        break
                    except ValueError:
                        print("Invalid choice, try again.")
                        continue
                elif key == "Format":
                    try:
                        print("Choose from the following options:")
                        print("1. LP, 2. 2xLP, 3. 3xLP, 4. 7\", 5. 10\", 6. 12\"")
                        formats = {1: "LP", 2: "2xLP", 3: "3xLP", 4: "7\"", 5: "10\"", 6: "12\""}
                        selected_format = int(input("Enter the choice: "))
                        if selected_format not in formats:
                            print("Invalid choice, please try again")
                            continue
                        print(f"Format chosen:, {formats[selected_format]}")
                        print("Is it a reissue, compilation or 180g etc?")
                        
                        while True:
                            choice = input("Yes or No: ")
                            if selected_format in [1, 2, 3]:
                                if choice.lower() == "yes" or choice.lower() == "y":
                                    record[key] = f"{formats[int(selected_format)]}, Album, {input('Enter the additional information: ')}"
                                    break
                                elif choice.lower() == "no" or choice.lower() == "n":
                                    record[key] = formats[selected_format]
                                    break
                                else:
                                    print("Invalid choice, please try again")
                            else:
                                if choice.lower() == "yes" or choice.lower() == "y":
                                    record[key] = f"{formats[selected_format]}, {input('Enter the additional information: ')}"
                                    break
                                elif choice.lower() == "no" or choice.lower() == "n":
                                    record[key] = formats[selected_format]
                                    break
                                else:
                                    print("Invalid choice, please try again")
                        break
                    except ValueError:
                        print("Invalid choice, please try again")
                        continue
                elif key == "Rating":
                    try: 
                        rating = int(input("Rating from 1-5: "))
                        if rating < 1 or rating > 5:
                            print("Invalid rating, please try again")
                            continue
                        record[key] = rating
                    except ValueError:
                        print("Invalid input, please try again")
                        continue
                elif key == "Released":
                    try:
                        year = int(input("Released: "))
                        if year <= 1900 or year > datetime.now().year + 1:
                            print("Invalid year, please try again")
                            continue
                        record[key] = year
                    except ValueError:
                        print("Invalid input, please try again")
                        continue
                elif key == "CollectionFolder":
                    folders = list(set([record['CollectionFolder'] for record in collection if record['CollectionFolder'] != ""]))
                    print("Choose from the pre-existing folders or leave empty to create a new one")
                    for i, folder in enumerate(folders):
                        print(f"{i+1}. {folder}")
                    try:
                        folder_choice = input("Enter the choice: ")
                        if folder_choice:
                            if folder_choice.isdigit():
                                record[key] = folders[int(folder_choice)-1]
                            else:
                                print("Invalid choice, please try again")
                                continue
                        elif not folder_choice:
                            record[key] = input("Enter the name of the new folder: ")
                    except ValueError:
                        print("Invalid input, please try again")
                        continue
                    break
                else: 
                    user_input = input(f"{key}: ")
                    try:
                        if input_types[key] == int:
                            record[key] = int(user_input)
                        else: 
                            record[key] = user_input
                    except ValueError:
                        print(f"Invalid input for {key}. Expected {input_types[key].__name__}.")
                        continue
                break
        print("Confirm the details of the record")
        for key, value in record.items():
            print(f"{key}: {value}")
        confirm = input("Confirm, Yes or No: ")
        if confirm.lower() == "yes" or confirm.lower() == "y":
            collection.append(record)
            print(f"Record {record['Title']} by {record['Artist']} added to the collection")
            break
        else:
            print("Record not added, would you want to modify something or try again?")
            print("1. Modify, 2. Try again, 3. Return to the main menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                collection.append(record)
                modify_record(collection, record)
                break
            elif choice == "2":
                continue
            elif choice == "3":
                break
            else:
                print("Invalid choice, returning to the main menu")
                break
    return collection
    
    
def search_collection(collection) -> list:
    """Function to search the collection

    Args:
        collection (list): collection as list of dictionaries

    Returns:
        list: collection, modified or not
    """
    print(", ".join(collection[0].keys()))
    search_key = input(f"Enter the search key, leave empty to search everything: ")
    search_term = input("Enter the search term: ")
    search_results = []
    for record in collection:
        if search_key == "":
            for key, value in record.items():
                if search_term.lower() in value.lower():
                    search_results.append(record)
                    break
        else:
            for key, value in record.items():
                if key == search_key and search_term.lower() in value.lower():
                    search_results.append(record)
                    break
    if not search_results:
        print("No results found")
    else:
        print(f"\nSearch results:")
        for i, record in enumerate(search_results):
            print(f"{i+1}")
            for key, value in record.items():
                if value == "":
                    continue
                else:
                    print(f"{key}: {value}")
        choice = input(f"Enter the number of the record to modify or delete, or leave empty to return to the main menu: ")
        if choice:
            print("1. Modify, 2. Delete, 3. Return to the main menu")
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    modify_record(collection, search_results[int(choice)-1])
                case "2":
                    collection.remove()
                case "3":
                    pass
    return collection

def modify_record(collection, record) -> list:
    """Function to modify a record in the collection

    Args:
        collection (list): collection as list of dictionaries
        record (dict): record to modify
        key (string): key to modify

    Returns:
        list: collection, modified
    """
    for key, value in record.items():
            print(f"{key}: {value}")
    try:
        key = input(f"Enter the key to modify, or leave empty to return to the main menu: ")
        if key in record:
            value = input(f"Enter the new value for {key}: ")
            record[key] = value
            print(f"Record {record['Title']} by {record['Artist']} modified in the collection")
        elif not key:
            print("Returning to the main menu")
    except KeyError:
        print(f"Incorrect key, please try again")    
    return collection

def delete_record(collection, record) -> list:
    """Function to delete a record from the collection

    Args:
        collection (list): collection as list of dictionaries
        record (dict): record to delete

    Returns:
        list: collection, modified
    """
    collection.remove(record)
    print(f"Record {record['Title']} by {record['Artist']} deleted from the collection")
    return collection

def list_collection(collection):
    """Function to list the collection
        Lists the collection by the keys selected or everything if no keys.
        Automatically removes spaces from the keys input
    Args:
        collection (list): collection as list of dictionaries
    """
    print("Select the keys you want to be listed, leave empty to list everything")
    print(", ".join(collection[0].keys()))
    keys = input("Enter the keys, separated by commas: ")
    if " " in keys:
        keys = keys.replace(" ", "")
    if keys:
        keys = keys.split(',')
        for record in collection:
            for key, value in record.items():
                if key in keys:
                    print(f"{key}: {value}")
            print("--------------------")            
    else:
        for record in enumerate(collection):
            for key, value in record.items():
                print(f"{key}: {value}")
    

def save_collection(collection, filename):
    """Function to save the collection to a .csv file
        Uses the filename from load_collection function to save the collection.
        Handles the case where the collection is empty or has abnormalities.
        Uses csv.DictWriter to write the collection to the csv file
    Args:
        collection (list): collection as list of dictionaries
        filename (string): filename to save the collection to
    """
    fieldnames = ['Catalog#', 'Artist', 'Title', 'Label', 'Format', 'Rating', 'Released', 'release_id', 'CollectionFolder', 'Date Added', 'Collection Media Condition', 'Collection Sleeve Condition', 'Collection Notes']
    standardized_collection = []
    for record in collection:
        standardized_record = {key: record.get(key, "") for key in fieldnames}
        standardized_collection.append(standardized_record)

    with open(f'{filename}', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in standardized_collection:
            if any(record.values()):  # Only write non-empty records
                writer.writerow(record)
    print(f"Collection saved to {filename}")
    
def print_stats(collection):
    """Function to print out statistics about the collection
        Counts the number of records, most common artist and average year of release
    Args:
        collection (_type_): Collection as list of dictionaries
    """
    artist_occurrences = {}
    years = []
    for record in collection:
        artist = record['Artist']
        year = record['Released']
        if year == "":
            continue
        try:
            year = int(year)
            if year <= 0 or year > datetime.now().year:
                continue
            years.append(year)
        except ValueError:
            continue
        if artist in artist_occurrences:
            artist_occurrences[artist] += 1
        else:
            artist_occurrences[artist] = 1
    if len(collection) < 1:
        print("You have no records in your collection")
    else:
        fav_artist = max(artist_occurrences, key=artist_occurrences.get) if artist_occurrences else "No favourite artist available"
        match years:
            case []:
                average_year_str = "No records with valid year of release available"
            case _:
                average_year = sum(years) / len(years)
                average_year_str = f"{average_year:.0f}"
        print(f"You have {len(collection)} records in your collection, your favourite artist is {fav_artist}, and the average year of release is {average_year_str}")
    
def main():
    collection, filename = load_collection()
    while True:
        print("---------------------------")
        print("Welcome to your offline vinyl collection!")
        print_stats(collection)
        print("Choose from the following options:")
        print("-------------------------------")
        print("1. Add a new record")
        print("2. Search and modify")
        print("3. List the collection")
        print("Leave empty to save and exit")
        print("-------------------------------")
        choice = input("Enter your choice: ")
        if len(collection) < 1 and choice in ['2', '3']:
            print("You have no records in your collection, please add some first.")
            continue
        elif choice == '1':
            collection = add_record(collection)
        elif choice == '2':
            collection = search_collection(collection)
        elif choice == '3':
            list_collection(collection)
        elif not choice:
            save_collection(collection, filename)
            break
        else:
            print("Invalid choice, please try again")
            
        save_collection(collection, filename)
            
        
if __name__ == "__main__":
    main()