## Class Main
### Objects
### __init__(filename)
Initializer that contains lists for different types of files. It also triggers the 
self.execute() function.
The lists:
    These lists are used in Main.check_file_type(). When searching through the different directories, the file names are appended to the lists which are then processed in Main.execute().

### check_one_file_and_search()
When a new instance is created and one single file needs to be checked, this function checks what file type it is and then triggers the search for it.

### check_file_type()
Organizes the files found in a folder based on its type and places the file names in its corresponding list. Starts at the user's home folder.

### execute()
Executes the search, maximizing CPU usage, on the lists provided by Main.__init__.
Utilizes the concurrent.futures library to make use of multiple threads.

## Class Search
This class provides methods that search strings for PII based on file type.

### char_search(a_string='')
This function checks a string for social security numbers and credit card numbers.
Returns a tuple containing the string that matches a form of PII or zero if no PII found in the string.

### line_cleanup_and_check(the_list=[],line_number=int,filename='',type_check='')
First it opens the txt files associated with the different file types.
Next it iterates over the list and checks if the string given is composed of only numbers.
Finally, it calls char_search() if the string only contains numbers.

### txt_search(file_read='')
Searches for PII in a txt file.
Reads line by line and creates a list of the strings found in the line. 
The sections are split by white-space but this can be changed.
Calls line_cleanup_and_check() on the list.

### csv_search(file_read='')
Searches for PII in a CSV file.
Same as txt search but sections are split by commas.

### convert_pdf_to_string(file_read='')
Converts text from a PDF file into a single string.

### pdf_search(file_read='')
Searches for PII in a PDF file.
The text of a PDF file is converted into a single string using the pdfminer.six library.
This string is then split by white-space and searched using char_seach().

### doc_search(file_read='')
Searches for PII in a Microsoft Word document.

### pptx_search(file_read='')
Seaches for PII in a Microsoft Powerpoint document.
Makes use of the pptx library.
First, it iterates through the slides looking for shapes that contain text. If it contains text, it calls line_cleanup_and_check() for the PII check.

### json_search(file_read='')
Searches for PII in a JSON file.
