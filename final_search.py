import re
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


class Search:
    def __init__(self):
        self.occurrences = open("exposed_files.txt", "a")
        self.files_checked = open("filesChecked.txt", "a")

    def char_search(self, a_string):
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
            return 0

    def txt_search(self, file_read):
        """Searches for PII in a txt file

        Args:
            file_read (FILE): A white-space delimited txt file
        """
        occurrences = open("exposed_files.txt", "a")

        with open(file_read, "r", encoding="utf-8") as file:
            self.files_checked.write(file_read.strip("./") + "\n")
            linecount = 0
            line = file.readline()
            while line:
                linecount += 1
                line = line.strip()
                line_list = line.split()
                for sect in line_list:
                    sect = sect.strip(",")
                    check_letters = sect.isalpha()
                    if (not check_letters) and (len(sect) > 8):
                        check_format = self.char_search(sect)

                        if check_format != 0:
                            filename = file_read.split(".//")
                            occurrences.write(
                                f"File: {filename[0]} Line Number: {linecount} Value: {check_format}\n"
                            )
                            occurrences.close()
                            file.close()
                            return

                line = file.readline()
            file.close()
        occurrences.close()

    def csv_search(self, file_read):
        """Searches for PII in a CSV file.

        Args:
            file_read (CSV): A comma delimited file.
        """

        with open(file_read, "r", encoding="utf-8") as file:
            self.files_checked.write(file_read.strip("./") + "\n")
            linecount = 0
            line = file.readline()
            while line:
                linecount += 1
                line_list = [x.strip() for x in line.split(",")]
                for sect in line_list:
                    check_letters = sect.isalpha()
                    if (not check_letters) and (len(sect) > 7):
                        check_format = self.char_search(sect)
                        if check_format != 0:
                            filename = file_read.split(".//")
                            filename = filename[0].strip("./")

                            self.occurrences.write(
                                f"File: {filename} Line Number: {linecount} Value: {check_format}\n"
                            )
                            self.occurrences.close()
                            file.close()
                            return
                    if linecount == 70:
                        return

                line = file.readline()
            file.close()
        self.occurrences.close()

    def convert_pdf_to_string(self, file_read):
        output_string = StringIO()
        with open(file_read, "rb") as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)

        return output_string.getvalue()

    def pdf_search(self, file_read):
        filename = file_read.split(".//")
        occurrences = open("exposed_files.txt", "a")
        text = self.convert_pdf_to_string(file_read)
        text_list = text.split()
        for item in text_list:
            result = self.char_search(item)
            if result != 0:
                occurrences.write(f"File: {filename[0]} Value: {result}\n")
                occurrences.close()
                return
