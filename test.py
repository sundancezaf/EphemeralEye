import os
import sys
import time
from pathlib import Path

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

"""


if len(sys.argv) > 1:
    filename = sys.argv[1]
    print(filename)
else:
    print("Nothing here")
