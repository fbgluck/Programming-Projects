# -*- coding: utf-8 -*-
"""
Created on Mon May 17 17:55:03 2021

@author: fgluck

Demonstrates a bit more sophistication using beautiful soup to scrape a webpage

"""
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:11:18 2021

@author: fgluck
"""
# This library allows you to send a http request to a website like a browser
import requests
# This is the beautifulSoup library for web scraping
from bs4 import BeautifulSoup
# set the url of the site you are going to scrape
url = "https://www.sanford.org/o/sanford-high-school/staff"
# set the headers to be sent along with the request
headers = {"Accept-Language": "en-US, en;q=0.5"}

# Now make the request to the URL and store the results 
results = requests.get(url, headers=headers)
# We'll print the result of the the request. 200 indicates it was successful
print(f'Web request returned: {results}')

# Now take the returned text and parse it into an object using BS
soup = BeautifulSoup(results.content, "html.parser")

# Use BS to pick out all items in the class
teachers=soup.find(class_= "page-container")
# and pick out all the items with a class of name
teacher_name= teachers.find_all(class_='name')

# iterate through the iterable and print each name
for x in teacher_name:
    # extract just the text from the element and strip all the spaces
    print(x.text.strip())
