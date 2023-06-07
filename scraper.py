import requests
from bs4 import BeautifulSoup

def getData(company):    
    # gets data
    url = f"https://www.wsj.com/search?query={company}&mod=searchresults_viewallresults"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    # parses HTML
    headlines = []
    blurbs = []

    soup = BeautifulSoup(response.text, 'html.parser')
    main = soup.find("main")
    articles = main.find_all("article")
    # iterates each chunk
    for i in articles:
        headline = i.find("h3")
        if headline != None:
            headlines.append(headline.a.span.text)

        blurb = i.find("p")
        if blurb != None:
            if blurb.span != None:
                blurbs.append(blurb.span.text)
    
    return [headlines, blurbs]

getData('nvidia')