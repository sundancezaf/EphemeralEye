# Import dependencies here
import os
import pandas

class main:
    def __init__(self):
        self.file_read = None
        self.check_file_type()
    
    def execute(self):
        firstT = no_extension_cleanup()
        firstT.cleanup()

    def check_file_type(self):
        for file in os.listdir("."):
            self.file_read = os.fsdecode(file)
            # Find extension type
            if self.file_read.endswith(".txt"):
                self.file_read = os.fsdecode(file)
                tryF = no_extension_cleanup()
                tryF.cleanup()
                #print("We got a text file\n")
                #print(self.file_read)
                #first = no_extension_cleanup(self.file_read)
                #first.cleanup(self.file_read)

        
class no_extension_cleanup(main):
    def __init__(self, file_read):
        super().__init__(file_read)

    def cleanup(self):
        print("Yo")
        '''Searches for social security numbers 
        
        occurrences = open("exposed_files.txt","w")

        with open(self.file_read, "r", encoding="utf-8") as file:
            count = 0
            line = file.readline()
            while line:
                if (("SSN" in line) or ("ssn" in line) or ("social security number" in line)):
                    count +=1
                    occurrences.write(str(count));
                    # Write to the text file which file contains the ssn
                    # Break from here because no need to search for other SSNs, one is enough

                    break
                line = file.readline()
            '''


class csv_files_cleanup():
    pass

class pdf_file_cleanup():
    pass

class SQL_database_cleanup():
    pass


first = main()

