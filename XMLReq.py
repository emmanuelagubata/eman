import requests
import json
import Recursive_json
from xml.etree import ElementTree

#Do a get request using the link below. We know this link returns XML. Take that XML and convert it to JSON.

keyword = "eye"

KeywordURL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term="+ keyword +"&tool=my_tool&email=my_email@example.com"