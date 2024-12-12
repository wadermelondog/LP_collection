# LP Collection

## Submission
**Introduction to Programming: Final Project Submission**  
### Lauri Turunen \[AG3154\]  
  
Link to project documentation:  
[Link](https://gitlab.labranet.jamk.fi/AG3154/loppuprojektitest)

4-5  
<br>  
**SELF-ASSESSMENT**

**Strengths**  
+ The application works as intended.  
+ I believe I utilized the techniques taught in the course quite well.  
+ CSV file handling works well.  
+ Input error handling is decent, even though `except` errors were only minimally used.  
+ The flowchart is a good addition, in my opinion.

**Areas for Improvement**  
- The `add_record` function became somewhat bloated. A helper function for handling keys and passing values in a dictionary for specific keys might have been better than using `elif` statements for different values.  
- Implementing the ability to press `Esc` at any point to return to the main menu was left undone.  
- I didn’t use custom classes or similar features, but I didn’t feel the need for them either.

### Basic Idea
A Python program to maintain my vinyl record collection.

### Functions
At least the following:

- **Search function for the collection**: Parameters can be almost any record attribute, such as condition or publisher.  
- **Add a new record**: Parameters include artist, album name, label, year, specific format (e.g., 2LP, 3LP, 180g, etc.), price, storage location (shelf/display case), star rating out of 5, additional notes, and date added. Essentially everything available in Discogs. Below are Discogs parameters:  
  `Catalog#, Artist, Title, Label, Format, Rating, Released, release_id, CollectionFolder, Date Added, Collection Media Condition, Collection Sleeve Condition, Collection Notes`.  
- **Edit record details**  
- **Delete a record**

#### Lauri Turunen 23/09/2024

## 26/10/2024 

**Project brainstorming and changes to functions.**  
Menu: Displays current collection statistics, e.g., the total number of records.  
1. Add a new record  
2. Search records  
   - Submenus for search: Edit record details and delete record  
3. List all records, with the option to list only specific details of the records  
4. Load a collection, with the possibility to create a new collection  
5. Wishlist: A basic way to keep track of records I’d like to have.  

I decided to implement the project so that the program loads a `.csv` file at startup as a dictionary, making it easier to handle, and then saves it back to `.csv` upon closing. In Python, the `DictReader` method can read a file as a list of dictionaries, using the header row as keys (e.g., catalog, name, etc.).

## 28/11/2024
Time to finalize this project.  
**15:40** Locked in.  
**17:40** Progressing well.  
**21:34** Done, with final comments, tweaks, and output formatting. The "average year" stat is still broken.

## 29/11/2024
The average year function somewhat works, but if there aren’t enough records, it throws a `ZeroDivisionError`, which needs fixing.  
Added features, for example:  
- In the "add record" function, the condition section now directly prompts you to select from predefined conditions for the sleeve and media.  
- The only issue is that it now freezes at that point :D. I tweaked it a bit, and in the format section, it now prompts you to input manually. Discogs’ format list is so long that I’ll likely stick with user input for now in this text-based program.  

![Format List](/Dokumentaatio/image.png)

## 04/12/2024
Good progress today. Spent several hours on this instead of my English assignments...  
- Added more error handling. I could almost create a custom error, but I didn’t feel like it.  
- Various tweaks...  
- Still lots of bugs, but the project is moving forward.

## 10/12/2024
More bug fixes and error handling.  
I’m considering adding a feature where settings (like the collection’s filename) are saved to a configuration file, which the program would automatically load.  
Maybe if I get really motivated, I could use an API to fetch collection averages, etc. This would require extensive error handling, though, and since Discogs already provides this directly, I’m not sure it’s worth it.  
I’m questioning the usefulness of the "list collection" feature. It might not be used as much as the search function, which is quite powerful.  
**TODO**: Add case-insensitive handling to everything.  
**23:34** Implemented a new function: confirmation. I use yes/no prompts so often that I decided to simplify by creating a dedicated function for it.  
Also started using WakaTime.

![Flowchart](/Dokumentaatio/flowchart.png)

## 11/12/2024
Case-insensitive handling and confirmation function completed.  
Got an idea to implement a "handle folders" function as the last feature. It could allow moving all search results to a different folder, for instance. I might add this later but will leave it as-is for now.
