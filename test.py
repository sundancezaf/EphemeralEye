import os
import sys
import re
import time
from pathlib import Path
import final_search
import main

# print(Path.home())
"""
start = time.perf_counter()
dirToSearch = "./testFiles"
 
count = 0
    
end = time.perf_counter()
print("--- %s seconds ---" % (end - start))

def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths


print(list_files(dirToSearch, '.txt'))




def check_txt_files(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            count += 1
            if count == 500:
                print(line)


if len(sys.argv) > 1:
    filename = sys.argv[1]
    print(filename)
    new = main.Main(filename)
else:
    print("Nothing here")

"""


def char_search(a_string):
    """This function checks a string for social security numbers and credit card numbers.

    Args:
        a_string (str): the string to search in

    Returns:
        int: returns 0 if no PII found
        tuple: key,value pair if PII found
    """
    pii_values = {
        "Amex": "^3[47][0-9]{13}$",
        "BCGlobal": "^(6541|6556)[0-9]{12}$",
        "Carte Blanche": "^389[0-9]{11}$",
        "Diners Club": "^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": "^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$",
        "Insta Payment": "^63[7-9][0-9]{13}$",
        "JCB": "^(?:2131|1800|35\d{3})\d{11}$",
        "Laser": "^(6304|6706|6709|6771)[0-9]{12,15}$",
        "Maestro": "^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$",
        "Master": "^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$",
        "Solo": "^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$",
        "Switch": "^(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}$",
        "Union Pay": "^(62[0-9]{14,17})$",
        "Visa": "^4[0-9]{12}(?:[0-9]{3})?$",
        "Social Security Number": "^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$",
    }
    a_string_list = a_string.split()
    for section in a_string_list:
        # Here is where you check if it matches the parameters
        for key, value in pii_values.items():
            value_search = re.search(str(value), section)
            if value_search:
                return key, section
        return 0


print(char_search("234-45-6789"))
