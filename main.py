from bs4 import BeautifulSoup
import urllib3

# Set the URL here
urlpage = "http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/"

# Helper method to filter the HTML node
def image_filter(tag):
    return tag.name == "img"

def fetch(urlpage):
    # query the website and return the html to the variable 'page'
    page = http.request("GET", urlpage)

    # parse the html using beautiful soup and store in variable 'soup'
    return BeautifulSoup(page.data, "html.parser")

http = urllib3.PoolManager()

soup = fetch(urlpage)

images = soup.find_all(image_filter)
[print(item["src"]) for item in images]
