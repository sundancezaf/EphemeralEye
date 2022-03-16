## Overall
- How to check that it is a social security number? Check the length of the string, has to be 




### Class no_extension_cleanup
- Do you need to show the number of occurrences




## Basic Algorithm
1. Start at parent folder then traverse the tree directory
2. For each folder
    Check each file type
    According to file type, open and check for PII
    Write if the file contains PII
3. Return after every folder has been checked


^(\d{3}[0-9]+(-[0-9]+)-[0-9]+)