# Import dependencies here
import os
import glob
import concurrent.futures
import re
import time
from search import *

start_time = time.time()


class Main:
    """This class contains methods to check the file types found in a folder, and a method to execute the
    search functions above.
    """

    def __init__(self):
        self.file_read = None
        self.csv_list = []
        self.txt_list = []
        self.check_file_type()
        self.execute()

    def check_file_type(self):
        """Organizes the files found in a folder based on its type and places the file names in its corresponding list"""
        counter = 0
        file_size_sum = 0
        directories = glob.glob("./**/", recursive=True)
        num_files = open("filesChecked.txt", "w")

        for item in directories:
            # print(item)
            for filename2 in os.listdir(item):
                filename3 = item + filename2

                if filename2.endswith(".txt") or filename2.endswith(".TXT"):
                    # print(filename3)
                    self.txt_list.append(filename3)

                if filename2.endswith("csv"):
                    # print(filename3)
                    self.csv_list.append(filename3)
        print(self.txt_list)
        print(self.csv_list)

    def execute(self):
        """Executes the search, maximizing CPU usage, on the lists provided by init."""

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(txt_search, self.txt_list)

        with concurrent.futures.ThreadPoolExecutor() as executor2:
            executor2.map(csv_search, self.csv_list)


first = Main()
print("--- %s seconds ---" % (time.time() - start_time))
