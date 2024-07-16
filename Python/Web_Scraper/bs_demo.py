# -*- coding: utf-8 -*-
"""

This is a simple code file demonstrating the use of Beautiful Soup
to scrape a local file webpage. The code for the webpage is included
at the end of this file.

"""
from bs4 import BeautifulSoup

with open("C:/Users/fgluck/Desktop/BS_testfile.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# Grab and return all the <h1> elements in the file as a list
all_h1 = soup.find_all('h1')
# display number of items returned and each item
print(f'There are: {len(all_h1)} <h1> elements in the list that was returned')
# print(all_h1)
for h1_elements in all_h1:
    print (h1_elements)
print ('==========================')
all_centered=soup.find_all('center')
print(f'There are; {len(all_centered)} <center> elements in the list that was returned')
for centered_elements in all_centered:
    print(centered_elements)
  
"""
<!-- This is the HTML page. Copy the following to a .html file on your desktop and change
the URL in line 8 to match -->

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>HTML Test Page</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
<h1>this is header 1 text - 0</h1>
<h2>This is header 2 text - 0</h2>
<h3>This is header 3 text - 0</h3>
<p>This is paragraph text - 0</p>
<p><center>This text is centered - 0 </center></p>
<hr>
<h1>this is header 1 text - 1</h1>
<h2>This is header 2 text - 1</h2>
<h3>This is header 3 text - 1</h3>
<p>This is paragraph text -1 </p>
<p><center>This text is centered - 1</center></p>
<hr>
</body>
</html>



"""

    