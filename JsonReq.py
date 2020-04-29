import requests
import json
import Recursive_json

#Here we do a get request and it returns data we parsed to JSON
#Now find a way to output the title, publish date
#you can use the Recursive_json import for this.

IdURL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=7152508&retmode=json&tool=my_tool&email=my_email@example.com"

r = requests.get(url = IdURL)

data = r.json()