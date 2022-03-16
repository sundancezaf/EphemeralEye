## Overall
- How to check that it is a social security number? Check the length of the string, has to be 

Need to conform to the standards provided in: https://treasury.fo.uiowa.edu/sites/treasury.fo.uiowa.edu/files/wysiwyg_uploads/ui_merchant_services-credit__policy_and_security_standards.pdf




## Information Searched
- Social Security Numbers
- Credit  Numbers
- Routing and Account Numbers
- Insurance Numbers?
- 



### Class no_extension_cleanup
- Do you need to show the number of occurrences




## Basic Algorithm
1. Start at parent folder then traverse the tree directory
2. For each folder
    Check each file type
    According to file type, open and check for PII
    Write if the file contains PII
3. Return after every folder has been checked



## Regex Expressions

SSN == "^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$"

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


    Credit Cards Dictionary:

    {"Amex":"^3[47][0-9]{13}$",
    "BCGlobal":"^(6541|6556)[0-9]{12}$",
    "Carte Blanche":"^389[0-9]{11}$",
    "Diners Club":"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
    "Discover":"^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$",
    "Insta Payment":"^63[7-9][0-9]{13}$",
    "JCB":"^(?:2131|1800|35\d{3})\d{11}$",
    "KoreanLocal":"^9[0-9]{15}$",
    "Laser":"^(6304|6706|6709|6771)[0-9]{12,15}$",
    "Maestro":"^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$",
    "Master":"^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$",
    "Solo":"^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$",
    "Switch":"^(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}$",
    "Union Pay":"^(62[0-9]{14,17})$",
    "Visa":"^4[0-9]{12}(?:[0-9]{3})?$",
    "Visa Master":"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$"}