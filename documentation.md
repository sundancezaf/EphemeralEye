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
First it opens the txt files 