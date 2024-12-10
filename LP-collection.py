import csv
from datetime import datetime
import os.path

def load_collection() -> tuple[list, str]:
    """Function to load the collection from a .csv file
        Asks for the filename to load the collection from, if empty, creates a new collection.
    Returns:
        tuple[list, str]: tuple with the collection and filename
    """
    while True:
        collection = []
        filename = input("Enter filename to load the collection from, leave empty for new collection: ")
        try:
            if filename == "":
                while True:
                    choice = str(input("Enter the name of the new collection without .csv, or leave empty for default: "))
                    if not choice:
                        choice = "collection"
                    if os.path.isfile(choice + ".csv"):
                        print("File already exists, please choose another name.")
                        continue
                    else:
                        print(f"Creating a new collection with the filename {choice}.csv")
                        collection = []
                        filename = choice + ".csv"
                        return collection, filename
            elif filename.endswith(".csv"):
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
            
                

def add_record(collection) -> list:
    """Function to add a record to the collection
        Automatically inserts the current date and time for the Date Added field.
        Checks which input type is expected for the field and asks for it.
        Asks for the condition of the record or sleeve by displaying the options for it.
        Asks for the format of the record by displaying the options for it.
        Asks for the rating of the record and makes sure it is 1-5
        Asks for the year of release and makes sure it is a valid year
        Asks for the folder of the record and displays the options for it and handles the addition of a new folder
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
                            choice = confirmation()
                            if selected_format in [1, 2, 3]:
                                if choice == True:
                                    record[key] = f"{formats[int(selected_format)]}, Album, {input('Enter the additional information: ')}"
                                    break
                                else:
                                    record[key] = formats[selected_format]
                                    break
                            else:
                                if choice == True:
                                    record[key] = f"{formats[selected_format]}, {input('Enter the additional information: ')}"
                                    break
                                else:
                                    record[key] = formats[selected_format]
                                    break         
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
                    if folders != []:
                        print("Choose from the pre-existing folders or leave empty to create a new one")
                    for i, folder in enumerate(folders):
                        print(f"{i+1}. {folder}")
                    try:
                        if folders == []:
                            print("No folders found, creating a new one")
                            record[key] = input("Enter the name of the new folder: ")
                            break
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
        confirm = confirmation()
        if confirm == True:
            collection.append(record)
            print(f"Record {record['Title']} by {record['Artist']} added to the collection")
            print("1. Add another record, 2. Return to the main menu")
            conf_choice = input("Enter your choice: ")
            if conf_choice == "1":
                continue
            elif conf_choice == "2":
                break
            else:
                print("Invalid choice, returning to the main menu")
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
    while True:
        search_key = input(f"Enter the search key, leave empty to search everything: ").lower()
        if search_key not in [key.lower() for key in collection[0].keys()] and search_key != "":
            print("Invalid key, please try again")
            continue
        else:
            break        
    search_term = input("Enter the search term: ").lower()
    search_results = []
    for record in collection:
        if search_key == "":
            for key, value in record.items():
                if search_term in value.lower():
                    search_results.append(record)
                    break
        else:
            for key, value in record.items():
                if key.lower() == search_key and search_term.lower() in value.lower():
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
        while True:
            if choice:
                try:
                    record_index = int(choice) - 1
                    if 0 <= record_index < len(search_results):
                        print("1. Modify, 2. Delete, 3. Return to the main menu")
                        mod_choice = input("Enter your choice: ")
                        match mod_choice:
                            case "1":
                                modify_record(collection, search_results[record_index])
                                break
                            case "2":
                                if confirmation():
                                    collection = delete_record(collection, search_results[record_index])
                                    break
                                else:
                                    print("Record not deleted")
                                    break
                            case "3":
                                break
                            case _:
                                print("Invalid choice")
                                continue
                except ValueError:
                    print("Invalid choice, please try again")
                    continue
                
                        
    return collection

def modify_record(collection, record) -> list:
    """Function to modify a record in the collection

    Args:
        collection (list): collection as list of dictionaries
        record (dict): record to modify
    Returns:
        list: collection, modified
    """
    print("Current details:")
    for key, value in record.items():
            print(f"{key}: {value}")
    try:
        while True:
            key_input = input(f"Enter the key to modify, or leave empty to return to the main menu: ").lower()
            if key_input == "":
                print("Returning to the main menu")
                break
            for key in record.keys():
                if key_input == key.lower():
                    value = input(f"Enter the new value for {key}: ")
                    record[key] = value
                    print(f"Record {record['Title']} by {record['Artist']} modified.")
                    break
            else:
                print("Invalid key, please try again")
                continue
            
            print("1. Modify another value, 2. Return to the main menu?")
            choice = input("Enter your choice: ")
            if choice == "1":
                continue
            elif choice == "2":
                break
            else:
                print("Invalid choice, returning to the main menu")
                break
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
        print(f"{keys}")
        for record in collection:
            for key in keys:
                print(f"{record.get(key, '')} ", end="")
            print("---------------------------")              
    else:
        for record in collection:
            for key, value in record.items():
                if value == "":
                    continue
                print(f"{key}: {value}")
            print("---------------------------")
    print("End of collection")
    choice = input("Press Enter to return to the main menu: ")
    if not choice:
        pass
    

def save_collection(collection, filename):
    """Function to save the collection to a .csv file
        Uses the filename from load_collection function to save the collection.
        Handles the case where the collection is empty or has abnormalities in the records.
        Uses csv.DictWriter to write the collection to the csv file
        Also writes only records that have any values in them, although this is also handled in the add record function.
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
            if any(record.values()):
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
        if artist == "":
            continue
        if artist in artist_occurrences:
            artist_occurrences[artist] += 1
        else:
            artist_occurrences[artist] = 1
    if len(collection) < 1:
        print("You have no records in your collection")
    else:
        max_count = max(artist_occurrences.values()) if artist_occurrences else 0
        fav_artists = [artist for artist, count in artist_occurrences.items() if count == max_count]
        fav_artists_str = ", ".join(fav_artists)
        fav_artist = fav_artists[0] if len(fav_artists) == 1 else ""
        match years:
            case []:
                average_year_str = "No records with valid year of release available"
            case _:
                average_year = sum(years) / len(years)
                average_year_str = f"{average_year:.0f}"
        if len(fav_artists) > 1:
            print(f"You have {len(collection)} records in your collection, your favourite artists are {fav_artists_str} with {max_count} records each, and the average year of release is {average_year_str}")      
        elif len(fav_artists) == 1:
            print(f"You have {len(collection)} records in your collection, your favourite artist is {fav_artist} with {max_count} records, and the average year of release is {average_year_str}")
        else:
            print(f"You have {len(collection)} records in your collection, the average year of release is {average_year_str}")
            
            
def confirmation() -> bool:
    """Function to ask for confirmation
        Asks for confirmation, returns True or false.
    Returns:
        bool: True or False
    """
    while True:
        choice = input("Yes or No: ")
        if choice.lower() == "yes" or choice.lower() == "y":
            return True
        elif choice.lower() == "no" or choice.lower() == "n":
            return False
        else:
            print("Invalid choice, please try again")
            continue

def main():
    collection, filename = load_collection()
    while True:
        print("---------------------------")
        print("Welcome to your record collection!")
        print_stats(collection)
        print("Choose from the following options:")
        print("-------------------------------")
        print("1. Add a new record")
        print("2. Search")
        print("3. List the collection")
        print("Leave empty to exit")
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
            print("Exiting the program")
            if confirmation():
                save_collection(collection, filename)
            break
        else:
            print("Invalid choice, please try again")
            continue
            
        
if __name__ == "__main__":
    main()