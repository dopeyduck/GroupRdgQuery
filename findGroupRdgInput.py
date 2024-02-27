import re
from lxml import etree

# Define the namespace
ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Get the included and excluded witnesses from the user
included_witnesses_input = input("Please enter included witnesses: ")
excluded_witnesses_input = input("Please enter excluded witnesses: ")

# Split the input strings by commas, tabs, and spaces, strip any leading or trailing whitespace from each witness, and convert the lists of witnesses to sets
included_witnesses = set(witness.strip() for witness in re.split('[, \t]+', included_witnesses_input))
excluded_witnesses = set(witness.strip() for witness in re.split('[, \t]+', excluded_witnesses_input))

# Get the path of the XML file from the user
xml_file_path = input("Please enter the path of the XML file: ")

# Get the limit number from the user and convert it to an integer
limit_number = int(input("Please enter the limit number: "))

# Open and parse the XML file
with open(xml_file_path, 'r') as file:
    tree = etree.parse(file)

# Iterate over all 'app' elements
for app in tree.xpath('//tei:app', namespaces=ns):
    rdgs = app.xpath('.//tei:rdg', namespaces=ns)
    wits = [set(rdg.get('wit', '').split()) for rdg in rdgs]

    # Check if any wit attribute contains at least the limit number of elements from the included witnesses and none from the excluded witnesses
    for wit in wits:
        if len(wit & included_witnesses) >= limit_number and not wit & excluded_witnesses:
            # If so, print the 'n', 'from', and 'to' attributes of the 'app'
            print(f"n: {app.get('n')}, from: {app.get('from')}, to: {app.get('to')}")
            break