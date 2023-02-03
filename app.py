import requests
from bs4 import BeautifulSoup

# use this to download/get the webpage data we need
response = requests.get("https://stackoverflow.com/questions")

# using this to pass the html content to,
# second parameter is type of parser
soup = BeautifulSoup(response.text, "html.parser")

# first parameter is a css selector
# which is a string that helps us find an element in an html document
# we first type . to specify a class, then write name of the class
# this will return a list, each item in the list is an instance of the tag class
questions = soup.select(".s-post-summary js-post-summary")

# question-hyperlink is the name of the class
# we used get text to get the text inside of the Span element
for question in questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(".vote-count-post").getText())
