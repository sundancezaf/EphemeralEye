# Import dependencies here
import os
import glob
import re
#import pandas
import time
start_time = time.time()


class main:
    def __init__(self):
        self.file_read = None
        self.check_file_type()
    
    def execute(self):
        firstT = no_extension_cleanup()
        firstT.cleanup()

    def check_file_type(self):
        directories = glob.glob('./**/', recursive=True)
        for item in directories:
            print(item)
            for filename2 in os.listdir(item):
                if (filename2.endswith(".txt") or filename2.endswith(".TXT")):
                    filename3 = item + "/" + filename2 
                    first_clean = no_extension_cleanup(filename3)
                    first_clean.cleanup()
                    #print(filename2)

        '''
        for directory in glob.glob('./**/', recursive=True):
            print(directory)
            for item in glob.glob(',*.TXT',recursive=True):
                print(item)
                #file_read = item
                #tryF = no_extension_cleanup(file_read)
                #tryF.cleanup()
            #for file in os.listdir("."):
            #file_read = os.fsdecode(file)
            # Find extension type
        '''
        '''
            if (file_read.endswith(".TXT") or file_read.endswith(".txt")):
                tryF = no_extension_cleanup(file_read)
                tryF.cleanup()
                
                try:
                    file_read = os.fsdecode(file)
                    tryF = no_extension_cleanup(file_read)
                    tryF.cleanup()
                except:
                    break
                    print("Ooops")
                    '''

                #print("We got a text file\n")
                #print(self.file_read)
                #first = no_extension_cleanup(self.file_read)
                #first.cleanup(self.file_read)
    

        
class no_extension_cleanup():
    def __init__(self, filetoRead):
        self.filetoRead = filetoRead
        self.pii_values = {"Amex":"^3[47][0-9]{13}$",
    "BCGlobal":"^(6541|6556)[0-9]{12}$",
    "Carte Blanche":"^389[0-9]{11}$",
    "Diners Club":"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
    "Discover":"^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$",
    "Insta Payment":"^63[7-9][0-9]{13}$",
    "JCB":"^(?:2131|1800|35\d{3})\d{11}$",
    "KoreanLocal":"^9[0-9]{15}$",
    "Laser":"^(6304|6706|6709|6771)[0-9]{12,15}$",
    "Maestro":"^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$",
    "Master":"^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$",
    "Solo":"^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$",
    "Switch":"^(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}$",
    "Union Pay":"^(62[0-9]{14,17})$",
    "Visa":"^4[0-9]{12}(?:[0-9]{3})?$",
    "Social Security Number":"^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$"}

    def cleanup(self):
        #print("Yo")clear
        #Searches for social security numbers 
        
        occurrences = open("exposed_files.txt","a")

        with open(self.filetoRead, "r", encoding="utf-8") as file:
            count = 0
            linecount = 0
            line = file.readline()
            while line:
                linecount +=1
                lineList = line.split(",")
                for section in lineList:
                    section = str(section)
                    for key,value in self.pii_values.items():
                        if (key=="Social Security Number"):
                            value_search = re.search(str(value),section)
                        else:
                            #section_stripped = section.strip("-")
                            section_stripped = section.strip(",")
                            section_stripped = section_stripped.strip()
                            value_search = re.search(str(value), section_stripped)

                        if value_search:
                            occurrences.write(f"File name: {self.filetoRead}, Line Number: {linecount}, Type: {key} \n")                 
                line = file.readline()
            


class csv_files_cleanup():
    pass

class pdf_file_cleanup():
    pass

class SQL_database_cleanup():
    pass


first = main()
print("--- %s seconds ---" % (time.time() - start_time))
