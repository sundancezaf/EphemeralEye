## Overall

Need to conform to the standards provided in: https://treasury.fo.uiowa.edu/sites/treasury.fo.uiowa.edu/files/wysiwyg_uploads/ui_merchant_services-credit__policy_and_security_standards.pdf

---------------

## Information Searched
- Social Security Numbers
- Credit  Numbers
- Routing and Account Numbers
- Insurance Numbers?

---------------

### Class no_extension_cleanup
- Do you need to show the number of occurrences

---------------

## Basic Algorithm
1. Start at parent folder then traverse the tree directory
2. For each folder
    Check each file type
    According to file type, open and check for PII
    Write if the file contains PII
3. Return after every folder has been checked

---------------

## Regex Expressions
These expressions look for Social Security Numbers and Credit Card Numbers

SSN Regex:

```
SSN == "^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$"
```
 Credit Card Numbers Regex: 

```
Credit s :
    Amex : ^3[47][0-9]{13}$
    BCGlobal: ^(6541|6556)[0-9]{12}$
    Carte Blanche : ^389[0-9]{11}$
    Diners Club : ^3(?:0[0-5]|[68][0-9])[0-9]{11}$
    Discover : ^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$
    Insta Payment : ^63[7-9][0-9]{13}$
    JCB : ^(?:2131|1800|35\d{3})\d{11}$
    KoreanLocal: ^9[0-9]{15}$
    Laser : ^(6304|6706|6709|6771)[0-9]{12,15}$
    Maestro : ^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$
    Master: ^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$
    Solo : ^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$
    Switch : ^(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}$
    Union Pay : ^(62[0-9]{14,17})$
    Visa : ^4[0-9]{12}(?:[0-9]{3})?$
    Visa Master : ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$
```

#### PII Values Dictionary
The above expressions but turned into a dictionary

```Python
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
```

---------------

## Data Sets
Some testing data sets

https://www.reddit.com/r/bigquery/wiki/datasets#wiki_hacker_news_.284_gb.29_

https://dumps.wikimedia.org/

---------------

## Testing Credit Card Numbers
Fake Credit Card Numbers

```
JCB, 3566000020000410, 02/2023, 123
Visa, 4005550000000019, 04/2023, 111
Visa, 4503300000000008, 04/2023, 431
Visa, 4205260000000005, 05/2023, 213
Visa, 4001270000000000, 05/2023, 222
Visa, 4012000033330026, 05/2023, 566
Visa, 4005562233445564, 03/2023, 212
Visa, 4311780000241409, 03/2023, 434
Visa, 4012000033330026, 02/2023, 121
Visa, 4311780000241417, 01/2023, 733
Discover, 6011000990099818, 12/2023, 333
Amex, 378282246310005, 05/2023
Discover, 6011000991300009, 12/2023
JCB, 3530111333300000, 03/2023
Mastercard, 5425233430109903, 04/2023
Mastercard, 2222420000001113, 08/2023
Mastercard, 2223000048410010, 09/2023
Visa, 4263982640269299, 02/2023, 837
```


### Single Rows 

```
 3566000020000410
 4005550000000019
 4503300000000008
 4205260000000005
 4001270000000000
 4012000033330026
 4005562233445564
 4311780000241409
 4012000033330026
 4311780000241417
 6011000990099818
 378282246310005
 6011000991300009
 3530111333300000
 5425233430109903
 2222420000001113
 2223000048410010
 4263982640269299
 4263-9826-4026-9299
```

---------------

## The Corrupted Files
Filename | Line Number
---- | ----
test2.txt | 8 
test2.txt | 9 # From here on out, the document will not be checked because it returned one positive resul so entire document needs to be reviewed
test2.txt | 10 # does not appear
test1. txt | 8 
idaho.txt | 37388
test3.txt | 770
test_4.txt | 12
credit_card_datasets | 1
UT.TXT | 433

---------------

## The Tests
Need to transform these into actual unit tests

#### Test 1
Checking length of section time: 2.7857153 seconds

#### Test 2
Files Checked: 8
Sum of file size: 2.9 MB
Time: 1.4293756

#### Test 3
Files Checked 8:
Sum of file size: 2.9 MB
Times: 1.28086


## TODO

1. Regex compile???? -- to cut time down