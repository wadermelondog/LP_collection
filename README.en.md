# LP collection
This is a project for my programming basics (python) course.
This .md file is just an AI translated version of the original, stuff on the top may be old.

### Basic idea
A simple program to update my LP-record collection

### Functions

Search function: practically any record parameter must be able to be used as a parameter, based on condition or even publisher.

Adding a new record: parameters include artist, record name, label, year, exact format, e.g., 2LP, 3LP, 180 grams, etc. Price? Which shelf or display case it is in.
Stars /5 and additional information as well as the date added, so practically everything that is also on Discogs. Below are the Discogs parameters.
Catalog#,Artist,Title,Label,Format,Rating,Released,release_id,CollectionFolder,Date Added,Collection Media Condition,Collection Sleeve Condition,Collection Notes

Editing record information

Deleting record information

#### Lauri Turunen 23/09/2024


## 26/10/2024 

Project brainstorming,
Changes to functions.
Menu: Shows stats about the collection at the moment, e.g., number of records
1. Add a new record
2. Search records
    Subprograms for search function, Edit record information and delete record
3. List all records, with the possibility to list only certain information about the records
4. Load collection, possibility to create a new collection
5. Wish list, a basic way to keep track of records I would like to have

I decided to implement the project so that the program loads a .csv file at the beginning as a dictionary, making it easier to handle, and then always saves it back to .csv when closing. In Python, there is a DictReader method that can read the file as a list of dictionaries and it feeds those dictionaries with keys from the top row like catalog, name, etc.

## 28/11/2024
Alright, now it's time to finish this up
15:40 Locked in
17:40 Looking good
21:34 Done, still need to add some clarifying comments and formatting the outputs, and the average year in the stats section is still broken

## 29/11/2024
The average year works somewhat, if there aren't enough records it gives a zerodivision error, needs fixing
Added stuff, for example in the add record section, the condition options now directly show the conditions to choose from, and then you can choose the condition of the sleeve, etc.
The only problem is that now it freezes at that point :D, I tweaked it a bit and in the format section, I added the same prompt and it just asks what to put.
The Discogs format list is just so long that probably at least in this text-based program, I'll end up letting the user input the extra information themselves.

![Format list](/Dokumentaatio/image.png)

## 04/12/2024
Good progress today, I've been working on this for several hours instead of doing English assignments...
Added more error handling, I could almost make my own error but haven't bothered...
All sorts of things...
Still a lot of bugs but got the project moving forward.

## 10/12/2024
More bug fixes and error handling.  
I thought maybe someday I could add a feature where there could be a settings file that saves, for example, the collection filename and it knows how to load it every time.  
Maybe if I get really excited someday, I could use an API to fetch the collection average or something. This would just require a lot of error handling, etc., and since Discogs already has it directly on their site, I'm not sure.
I'm starting to question the list collection feature a bit, it might not be used as much as the search function since the search function is quite good...
TODO: case insensitive handling for everything  
23:34, implementing a new function, confirmation. I use that yes or no thing so much that I'll just make it a separate function to make it easier.
I also started using Wakatime

![Flowchart](/Dokumentaatio/flowchart.png)

## 11/12/2024
Case insensitive handling and confirmation function done.
