from PyPDF2 import PdfFileReader
import re


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
        # Here is where you check if it matches the parameters
        for key, value in pii_values.items():
            value_search = re.search(str(value), section)
            if value_search:
                return key, section
                # print(key, section)
        return 0


def extraction(file_read):
    # occurrences = open("exposed_files.txt", "a")
    # files_checked = open("filesChecked.txt", "a")
    # files_checked.write(file_read)

    reader = PdfFileReader(file_read)
    # pages = reader.pages
    first_p = reader.getPage(0)
    text = first_p.extract_text()
    print(text)
    # print(first_p)

    """

    for page in pages:
        page2 = pages.extract_text()
        page2 = page2.strip()
        print(page2)

        # page_list = page2.split("\n")

        
        for item in page_list:
            item2 = item.replace(" ", "")
            print(item2)
            
            check_letters = item.isalpha()
            if (not check_letters) and (len(item) > 8):
                print(item)
                check_format = char_search(item)
                ##if check_format != 0:
                # filename = file_read.split(".//")
                # occurrences.write(f"File: {filename[0]} Value: {check_format}\n")
                # files_checked.close()
                # occurrences.close()
                # return
                return
                """

    # files_checked.close()
    # occurrences.close()
    # print(page2)
    # print(type(page2))
    # for line in page.readlines():
    # print(line)
    # print(page.extract_text())


def text_cleanup(text):
    text_list = text.split()
    translation = {
        33: "",
        34: "",
        35: "",
        36: "",
        37: "",
        38: "",
        39: "",
        40: "",
        41: "",
        42: "",
        43: "",
        44: "",
        46: "",
        47: "",
        58: "",
        59: "",
        60: "",
        61: "",
        62: "",
        63: "",
    }
    for text in text_list:
        text = text.translate(translation)
        print(text)


# cleextraction("test3.pdf")
extraction("test2.pdf")
# text_cleanup("what 123-422-4333,.;*")
