# Import dependencies here
import os
import glob
import concurrent.futures
import re
#import pandas
import time
start_time = time.time()

def char_search(aString):
        pii_values = {"Amex":"^3[47][0-9]{13}$",
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
        aStringList = aString.split()
        for section in aStringList:
            # Here is where you check if it matches the parameters
            for key,value in pii_values.items():
                value_search = re.search(str(value),section)
                if value_search:
                    return key, section
                    #print(key, section)
            return 0

def txt_search (file_read):
    occurrences = open("exposed_files.txt","a")
    files_checked = open("filesChecked.txt","a")
    with open(file_read, "r", encoding="utf-8") as file:
        files_checked.write(file_read + "\n")
        linecount = 0
        line = file.readline()
        while line:
            linecount += 1
            line = line.strip()
            #print(line)
            lineList = line.split()
            for sect in lineList:
                sect = sect.strip(",")
                #print(sect)
                check_letters = sect.isalpha()
                if (not check_letters) and (len(sect) > 8):
                    check_format = char_search(sect)
                    

                    if check_format != 0:
                        #count += 1
                        filename = file_read.split(".//")
                        occurrences.write(f"File name: {filename[0]} Line Number: {linecount} Value: {check_format}\n")
                        occurrences.close()
                        file.close()
                        return
                                                    
            line = file.readline()
        file.close()
    occurrences.close() 


def csv_search(file_read):
    occurrences = open("exposed_files.txt","a")
    files_checked = open("filesChecked.txt","a")
    with open(file_read, "r", encoding="utf-8") as file:
        files_checked.write(file_read + "\n")
        linecount = 0
        line = file.readline()
        while line:
            linecount += 1
            lineList = [x.strip() for x in line.split(',')]
            for sect in lineList:
                #print(sect)
                check_letters = sect.isalpha()
                if (not check_letters) and (len(sect) > 7):
                    #print(sect)
                    check_format = char_search(sect)
                    #(check_format)
                    if check_format != 0:
                        #count += 1
                        filename = file_read.split(".//")

                        occurrences.write(f"File name: {filename[0].strip('./')} Line Number: {linecount} Value: {check_format}\n")
                        occurrences.close()
                        file.close()
                        return
                if linecount == 70:
                    return
                                                    
            line = file.readline()
        file.close()
    occurrences.close()


class main:
    def __init__(self):
        self.file_read = None
        self.csv_list = []
        self.txt_list = []
        self.check_file_type()
        self.execute()
            

    def check_file_type(self):
        """Checks for types of file
        """    
        counter = 0
        file_size_sum = 0
        directories = glob.glob('./**/', recursive=True)
        num_files = open("filesChecked.txt","w")


        for item in directories:
            #print(item)
            for filename2 in os.listdir(item):
                filename3 = item + filename2 

                if (filename2.endswith(".txt") or filename2.endswith(".TXT")):
                    #print(filename3)
                    self.txt_list.append(filename3)
                    
                if (filename2.endswith("csv")):
                    #print(filename3)
                    self.csv_list.append(filename3)
        print(self.txt_list)
        print(self.csv_list)

   

    

    def execute(self):

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(txt_search, self.txt_list)
        
        with concurrent.futures.ThreadPoolExecutor() as executor2:
            executor2.map(csv_search, self.csv_list)


class pdf_file_search():
    pass

class SQL_database_search():
    pass


first = main()
print("--- %s seconds ---" % (time.time() - start_time))
