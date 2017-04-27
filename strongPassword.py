#! python 3
# program to check if a password is string or not
# min 8 characters, one upper, one lower, one number

import re

def strongPassword(password):
    upperRegex=re.compile(r'[A-Z].*')
    lowerRegex=re.compile(r'[a-z].*')
    numRegex=re.compile(r'\d.*')
    if len(password) < 8:
        print('Password must be minimum 8 characters')
    elif numRegex.search(password) == None:
        print('One character must be a number')
    elif lowerRegex.search(password) == None:
        print('One character must be a lowercase character')
    elif upperRegex.search(password) == None:
        print('One character must be an uppercase character')
    else:
        print('Pass word accepted')

print('Please enter password:')
password=input()

strongPassword(password)

