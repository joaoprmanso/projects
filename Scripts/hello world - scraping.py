from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib2 import urlopen as uReq  # Web client

# setting the url to download the data from
my_url = 'https://www.farfetch.com/pt/shopping/men/clothing-2/items.aspx?view=180&sort=4'


# setting up the connection and downloading the page data
uClient = uReq(my_url)


# reads the html data
page_html = uClient.read()
uClient.close()

farfetch_website = soup(page_html, "html.parser")
# print farfetch_website.span

# collects the information of the product
product_info = farfetch_website.findAll("div", {"data-test": "information"})
# print product_info[0]

# save the index in a new variable
contain = product_info[0]
container = product_info[0]


# print container.div

for i in range(1, 100):
    if i % 2 == 0:
        print i
    else:
        print "This number is odd"
