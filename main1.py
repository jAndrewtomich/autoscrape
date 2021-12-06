import requests # http requests
from bs4 import BeautifulSoup # parse html tags
import re # regular expressions
import sys # application argument parsing

# exceptions
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

url = "https://www.ted.com/talks/madhavi_venkatesan_the_life_cycle_of_a_pair_of_jeans#t-1189"

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")