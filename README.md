# Ephemeral Eye

This program searches entire directories for files that contain PII including social security numbers, credit card numbers, routing and account numbers, and insurance numbers.
It can also perform the PII check on a single file.

## How to Run

1. To run starting from home directory, checking all files:

```python
python3 main.py
```

2. To run on a single file

```python
python3 main.py [FILENAME]
```

#### Running a quick test
After cloning the repo, the folder testFiles contains small files to test the program on.

## Dependencies
These will be fixed once the program is packaged. until then, pip install the following:

```
1. pdfminer.six
2. docx2txt
```
