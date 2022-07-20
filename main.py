# Import dependencies here
import os
import sys
import time
import concurrent.futures
from pathlib import Path
import final_search

start = time.perf_counter()


class Main:
    """This class contains methods to check the file types found in a folder,
    and a method to execute search functions based on file type."""

    def __init__(self, filename):
        self.file_read = None
        self.csv_list = []
        self.txt_list = []
        self.pdf_list = []
        self.json_list = []
        self.doc_list = []
        self.pptx_list = []
        self.check_file_type()
        self.filename = filename
        self.execute()

    def check_one_file_and_search(self):
        new_search = final_search.Search()
        if self.filename.lower().endswith(".csv"):
            new_search.csv_search(self.filename)
        if self.filename.lower().endswith(".txt"):
            new_search.txt_search(self.filename)
        if self.filename.lower().endswith(".pdf"):
            new_search.pdf_search(self.filename)
        if self.filename.lower().endswith(".json"):
            new_search.json_search(self.filename)
        if self.filename.lower().endswith(".docx"):
            new_search.doc_search(self.filename)
        if self.filename.lower().endswith(".pptx"):
            new_search.pptx_search(self.filename)

    def check_file_type(self):
        """Organizes the files found in a folder based on its type
        and places the file names in its corresponding list"""

        home = str(Path.home())

        # directories = glob.glob("~", recursive=True)
        for root, dirs, files in os.walk(home):
            directory = root
            for filename2 in os.listdir(directory):
                filename2 = filename2.lower()
                filename3 = directory + "/" + filename2

                if filename2.endswith(".txt"):
                    self.txt_list.append(filename3)

                if filename2.endswith("csv"):
                    self.csv_list.append(filename3)

                if filename2.endswith("pdf"):
                    # print(filename3)
                    self.pdf_list.append(filename3)

                if filename2.endswith("json"):
                    self.json_list.append(filename3)

                if filename2.endswith("docx"):
                    self.doc_list.append(filename3)

                if filename2.endswith("pptx"):
                    self.pptx_list.append(filename3)

    def execute(self):
        """Executes the search, maximizing CPU usage, on the lists provided by init."""

        if self.filename != None:
            self.check_one_file_and_search()
        else:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                search_exec = final_search.Search()
                executor.map(search_exec.txt_search, self.txt_list)

            with concurrent.futures.ThreadPoolExecutor() as executor2:
                search_exec2 = final_search.Search()
                executor2.map(search_exec2.csv_search, self.csv_list)
        """
            with concurrent.futures.ThreadPoolExecutor() as executor3:
                search_exec3 = final_search.Search()
                executor3.map(search_exec3.pdf_search, self.pdf_list)

            with concurrent.futures.ThreadPoolExecutor() as executor4:
                search_exec4 = final_search.Search()
                executor4.map(search_exec4.json_search, self.json_list)
        """


if __name__ == "__main__":

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        # print(filename)
        new = Main(filename)
    else:
        new = Main(None)
        # new.execute()


end = time.perf_counter()
print("--------------------------------------")
print("Completed in: %.2f seconds " % (end - start))
print("\n")
print("--------------------------------------")
