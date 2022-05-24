"""
Quick testing script to check if a string contains only integers and then searches for
PII.
"""
import re


def find_alpha(a_string):
    """Check if a string contains only numbers and then it checks for PII

    Things to check for:
        1. If it's all alpha characters, don't search
        2. Search if greater than certain length
        3. Search only if above conditions are met


    Args:
        a_string (str): A simple string.

    Returns:
        int: returns 0 if it contains letters
        tuple: returns a key,value pair if it contains PII
    """

    continue_check = True
    pii_values = {
        "Amex": "^3[47][0-9]{13}$",
        "BCGlobal": "^(6541|6556)[0-9]{12}$",
        "Carte Blanche": "^389[0-9]{11}$",
        "Diners Club": "^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": "^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$",
        "Insta Payment": "^63[7-9][0-9]{13}$",
        "JCB": "^(?:2131|1800|35\d{3})\d{11}$",
        "KoreanLocal": "^9[0-9]{15}$",
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
        # Check if it's all alpha chars again
        check1 = str(section).isalpha()
        if not check1:
            # Here is where you check if it matches the parameters
            for key, value in pii_values.items():
                value_search = re.search(str(value), section)
                if value_search:
                    return key, section
                    # print(key, section)d
        return 0


with open("test1.txt", "r") as file1:
    count = 0
    line = file1.readline()
    while line:
        line = line.strip()
        # print(type(line))
        is_all_alpha = line.isalpha()
        if is_all_alpha:
            count += 1
            # print(count)
        else:
            check2 = find_alpha(line)
            if check2 != 0:
                print(check2)

        line = file1.readline()

file1.close()
# print(count)
