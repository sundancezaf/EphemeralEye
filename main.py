# Import dependencies here
import os
import re
#import pandas

class main:
    def __init__(self):
        self.file_read = None
        self.check_file_type()
    
    def execute(self):
        firstT = no_extension_cleanup()
        firstT.cleanup()

    def check_file_type(self):
        for file in os.listdir("."):
            file_read = os.fsdecode(file)
            # Find extension type
            if file_read.endswith(".txt"):
                file_read = os.fsdecode(file)
                tryF = no_extension_cleanup(file_read)
                tryF.cleanup()
                #print("We got a text file\n")
                #print(self.file_read)
                #first = no_extension_cleanup(self.file_read)
                #first.cleanup(self.file_read)
    

        
class no_extension_cleanup():
    def __init__(self, filetoRead):
        self.filetoRead = filetoRead

    def cleanup(self):
        #print("Yo")
        #Searches for social security numbers 
        
        occurrences = open("exposed_files.txt","w")

        with open(self.filetoRead, "r", encoding="utf-8") as file:
            count = 0
            linecount = 0
            line = file.readline()
            while line:
                linecount +=1
                first = re.search("^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$",line)
                if (first):
                        occurrences.write(f"Line Number {linecount} \n")
                        break                
                line = file.readline()
            


class csv_files_cleanup():
    pass

class pdf_file_cleanup():
    pass

class SQL_database_cleanup():
    pass


first = main()

