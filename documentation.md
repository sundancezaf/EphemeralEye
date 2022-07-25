# EphemeralEye
This program searches entire directories for files that contain PII. It can also perform the PII check on a single file. 

Files need to conform to the standards provided in: https://treasury.fo.uiowa.edu/sites/treasury.fo.uiowa.edu/files/wysiwyg_uploads/ui_merchant_services-credit__policy_and_security_standards.pdf

### Information Searched
- Social Security Numbers
- Credit Card Numbers
- Routing Numbers
- Medical Record Numbers
- ITIN numbers

## Class Main
### Objects
### __init__(filename)
Initializer that contains lists for different types of files. It also triggers the 
self.execute() function.
The lists:
    These lists are used in Main.check_file_type(). When searching through the different directories, the file names are appended to the lists which are then processed in Main.execute().

### check_one_file_and_search()
When a new instance is created and one single file needs to be checked, this function checks what file type it is and then triggers the search for it. This is triggered when a filename is given as an argument when starting the program.

### check_file_type()
Organizes the files found in a folder based on its type and places the file names in its corresponding list. Starts at the user's home folder.

### execute()
Executes the search, maximizing CPU usage, on the lists provided by Main.__init__.
Utilizes the concurrent.futures library to make use of multiple threads.

### second_execute()
Executes the second part of the search after first execute() is finished. This seach is json, docx, and pptx files. Function is called by the first execute().

## Class Search
This class provides methods that search strings for PII based on file type.

### char_search(a_string='')
Checks a string for social security numbers and credit card numbers.
Returns a tuple containing the string that matches a form of PII or zero if no PII found in the string.

### line_cleanup_and_check(the_list=[],line_number=int,filename='',type_check='')
First, it opens the txt files associated with the different file types.
Next, it iterates over the list and checks if the string given is composed of only numbers.
Finally, it calls char_search() if the string only contains numbers.
If it's a file that can be processed without an external library, it will 
take the original linecount, otherwise it will give it a starting linecount. This might differ than the original file as the linecount is done by sections that are split.

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

### docx_search(file_read='')
Searches for PII in a Microsoft Word document.

### pptx_search(file_read='')
Searches for PII in a Microsoft Powerpoint document.
Makes use of the pptx library.
First, it iterates through the slides looking for shapes that contain text. If it contains text, it calls line_cleanup_and_check() for the PII check.

### json_search(file_read='')
Searches for PII in a JSON file.

### Miscellaneous
Using concurrent.futures.ProcessPoolExecutor() instead of ThreadPoolExecutor() utilizes more of the CPU but for shorter periods of time.


## Testing

### The Corrupted Files
Filename | Line Number | Type
---- | ----
txt_test_2| 8 |
txt_test_2 | 9 | Credit Card
txt_test_2 | - | MRN
txt_test_2| 10 |
txt_test_1 | 8 | SSN
txt_idaho_names| 37388 |
txt_test_3 | 770 | SSN
txt-test-5 | 844| MRN
txt_test_4 | 12 | Credit Card


csv_ut_test.csv | 433 |
json_test_1 | - | SSN
ppt_test_1| - | SSN
word_test_1 | - | -
word_test_2 | - | -
ppt_test_1 | - | - 


### Credit Cards 
Some fake numbers to test: 

JCB, 3566000020000410, 02/2023, 123
Visa, 4005550000000019, 04/2023, 111
Visa, 4503300000000008, 04/2023, 431
Visa, 4205260000000005, 05/2023, 213
Visa, 4001270000000000, 05/2023, 222
Visa, 4012000033330026, 05/2023, 566
Visa, 4005562233445564, 03/2023, 212
Visa, 4311780000241409, 03/2023, 434
Visa, 4012000033330026, 02/2023, 121
Visa, 4311780000241417, 01/2023, 733
Discover, 6011000990099818, 12/2023, 333
Amex, 378282246310005, 05/2023
Discover, 6011000991300009, 12/2023
JCB, 3530111333300000, 03/2023
Mastercard, 5425233430109903, 04/2023
Mastercard, 2222420000001113, 08/2023
Mastercard, 2223000048410010, 09/2023
Visa, 4263982640269299, 02/2023, 837