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

    def __init__(self):
        self.file_read = None
        self.csv_list = []
        self.txt_list = []
        self.pdf_list = []
        self.json_list = []
        self.check_file_type()
        self.execute()

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

                if (filename2.endswith(".txt")) and (
                    (filename2 != "exposed_files.txt")
                    and (filename2 != "filesChecked.txt")
                ):
                    # print(filename3)
                    self.txt_list.append(filename3)

                if filename2.endswith("csv"):
                    # print(filename3)
                    self.csv_list.append(filename3)

                if filename2.endswith("pdf"):
                    # print(filename3)
                    self.pdf_list.append(filename3)

                if filename2.endswith("json"):
                    self.json_list.append(filename3)

        # print(self.txt_list)cd
        # print(self.csv_list)
        # print(self.pdf_list)

    def execute(self):
        """Executes the search, maximizing CPU usage, on the lists provided by init."""

        if len(sys.argv) > 1:
            start_file = sys.argv[1]
            self.check_file_type(start_file)
            for item in self.csv_list:
                final_search.Search()
            for item in self.txt_list:
                final_search.Search()
            for item in self.csv_list:
                final_search
            for item in self.json_list:
                final_search.Search()
            for item in self.pdf_list:
                final_search.Search()

        else:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                search_exec = final_search.Search()
                executor.map(search_exec.txt_search, self.txt_list)

            with concurrent.futures.ThreadPoolExecutor() as executor2:
                search_exec2 = final_search.Search()
                executor2.map(search_exec2.csv_search, self.csv_list)

            with concurrent.futures.ThreadPoolExecutor() as executor3:
                search_exec3 = final_search.Search()
                executor3.map(search_exec3.pdf_search, self.pdf_list)

            with concurrent.futures.ThreadPoolExecutor() as executor4:
                search_exec4 = final_search.Search()
                executor4.map(search_exec4.json_search, self.json_list)


if __name__ == "__main__":
    first = Main()
    end = time.perf_counter()
    print("--------------------------------------")
    print("--- %s seconds ---" % (end - start))
    print("\n")
    print("Results can be found in the exposed_files.txt file\n")
    print("--------------------------------------")
