# Regex syntax for matching a specific number of repetitions

import re

batRegex = re.compile(r'Bat(wo)?man') # can appear 1 or zero times
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo == None)

# look for phone numbers that do or do not have an area code
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

# look for phone numbers that do or do not have an area code
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo == True)

# Changing pattern so area code can appear 1 or zero times
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 543-555-1234. Call me tomorrow.')
print(mo.group())
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo.group())