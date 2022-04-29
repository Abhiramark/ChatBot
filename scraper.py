import os
import json
import datetime
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# we use this to get api key from env files
load_dotenv()
Dev_Token = os.getenv('Dev_Token')

'''
💡Use this version if you deploying it on repl.it
# Getiing bot token from env file
Dev_Token = os.environ['Dev_Token']

'''


# Getting TLDR articales
def currentDate():
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%d")
    return date

# Scrapping data from tldr page


def tldrData():
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%d")
    url = 'https://tldr.tech/newsletter/' + date
    print(url+"\nSending Data...")
    response = requests.get(url)
    # check response status
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
    # find all div tag with class mt-3
        divs = soup.find_all('div', class_='mt-3')
        for content in divs:
            rawData = content.text.strip()
            # clear new line from data
            data = rawData.replace('\n\n', '')
            # firsthalf
            firsthalf = data.split('\n')[2:9]
            # secondhalf
            secondhalf = data.split('\n')[9:16]
            # thirdHalf
            thirdHalf = data.split('\n')[16:24]
            # fourthHalf
            fourthHalf = data.split('\n')[24:32]

            # Addinf data and then replacinf ir with new line
            firsthalf = '\n'.join(firsthalf).replace('\n', '\n\n')
            secondhalf = '\n'.join(secondhalf).replace('\n', '\n\n')
            thirdHalf = '\n'.join(thirdHalf).replace('\n', '\n\n')
            fourthHalf = '\n'.join(fourthHalf).replace('\n', '\n\n')
            print("TLDR Sent Succesfully 🚀")

            return (firsthalf, secondhalf, thirdHalf, fourthHalf)

    else:
        print("No articles today")
        return ("Sorry, on "+date+" there is no new article on tldr.tech ☹️")


# Getting Devtop Top articles:


def devtoTop():
    url = "https://dev.to/api/articles/"
    res = requests.get(url, headers={"Api-Key": Dev_Token})
    data = res.json()

    title = data[0].get("title")
    desc = data[0].get("description")
    url = data[0].get("url")

    title1 = data[1].get("title")
    desc1 = data[1].get("description")
    url1 = data[1].get("url")

    title2 = data[2].get("title")
    desc2 = data[2].get("description")
    url2 = data[2].get("url")

    title3 = data[3].get("title")
    desc3 = data[3].get("description")
    url3 = data[3].get("url")

    title4 = data[4].get("title")
    desc4 = data[4].get("description")
    url4 = data[4].get("url")

    title5 = data[5].get("title")
    desc5 = data[5].get("description")
    url5 = data[5].get("url")

    topArticles = 'Dev.to Top Article 🧑‍💻\n'+'\n'+'Article : '+title+'\n\n' + \
        'Description : '+desc+'\n\n'+'Read Full article at : '+url+'\n\n' +\
        '--------x--------'+'\n\n'+'Article_01 : '+title1+'\n\n' + \
        'Description : '+desc1+'\n\n'+'Read Full article at : '+url1+'\n\n'\
        '--------x--------'+'\n\n'+'Article_02 : '+title2+'\n\n' + \
        'Description : '+desc2+'\n\n'+'Read Full article at : '+url2+'\n\n'\
        '--------x--------'+'\n\n'+'Article_03 : '+title3+'\n\n' + \
        'Description : '+desc3+'\n\n'+'Read Full article at : '+url3+'\n\n'\
        '--------x--------'+'\n\n'+'Article_04 : '+title4+'\n\n' + \
        'Description : '+desc4+'\n\n'+'Read Full article at : '+url4+'\n\n'\
        '--------x--------'+'\n\n'+'Article_05 : '+title5+'\n\n' + \
        'Description : '+desc5+'\n\n'+'Read Full article at : '+url5+'\n\n'

    print('Devto top articles sent succesfully 🚀')
    return topArticles

# Getting latest articles from devto


def devtoLatest():
    latest = "https://dev.to/api/articles/latest"
    latestRes = requests.get(latest, headers={"Api-Key": Dev_Token})
    data = latestRes.json()

    newtitle = data[0].get("title")
    newdesc = data[0].get("description")
    newurl = data[0].get("url")

    newtitle1 = data[1].get("title")
    newdesc1 = data[1].get("description")
    newurl1 = data[1].get("url")

    newtitle2 = data[2].get("title")
    newdesc2 = data[2].get("description")
    newurl2 = data[2].get("url")

    newtitle3 = data[3].get("title")
    newdesc3 = data[3].get("description")
    newurl3 = data[3].get("url")
    newtitle4 = data[4].get("title")
    newdesc4 = data[4].get("description")
    newurl4 = data[4].get("url")

    newtitle5 = data[5].get("title")
    newdesc5 = data[5].get("description")
    newurl5 = data[5].get("url")

    latestArticles = 'Dev.to Latest Article 🧑‍💻\n'+'\n'+'Article : '+newtitle+'\n\n' + \
        'Description : '+newdesc+'\n\n'+'Read Full article at : '+newurl+'\n\n' +\
        '--------x--------'+'\n\n'+'Article_01 : '+newtitle1+'\n\n' + \
        'Description : '+newdesc1+'\n\n'+'Read Full article at : '+newurl1+'\n\n'\
        '--------x--------'+'\n\n'+'Article_02 : '+newtitle2+'\n\n' + \
        'Description : '+newdesc2+'\n\n'+'Read Full article at : '+newurl2+'\n\n'\
        '--------x--------'+'\n\n'+'Article_03 : '+newtitle3+'\n\n' + \
        'Description : '+newdesc3+'\n\n'+'Read Full article at : '+newurl3+'\n\n'\
        '--------x--------'+'\n\n'+'Article_04 : '+newtitle4+'\n\n' + \
        'Description : '+newdesc4+'\n\n'+'Read Full article at : '+newurl4+'\n\n'\
        '--------x--------'+'\n\n'+'Article_05 : '+newtitle5+'\n\n' + \
        'Description : '+newdesc5+'\n\n'+'Read Full article at : '+newurl5+'\n\n'

    print('Devto latest articles sent succesfully 🚀')
    return latestArticles


# Getting latest archived articles from medium {technology}
def get_medium():
    url = "https://medium.com/tag/technology"
    res = requests.get(url, headers={
                       "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
    # print(res.status_code)
    soup = BeautifulSoup(res.text, 'html.parser')
    # h1 = soup.find_all('h1')
    # h2 = soup.find_all('h2')
    # h3 = soup.find_all('h3')
    a = soup.find_all('a', class_=(
        'au av aw ax ay az ba bb bc bd be bf bg bh bi'))
    art = soup.find_all('div', class_=('l ep kf'))
    # Declaring arr so after looping values can be store inside it
    artArray = []
    for x in art:
        # print(da)
        postUrl = x.find('a')
        # all titles are in h2 tag
        heading = x.find(
            'h2', class_="bn fw kl km kn ko ga kp kq kr ks ge kt ku kv kw gi kx ky kz la gm lb lc ld le gq gr gs gt gv gw fu")
        title = heading.contents[0]
        # Getting the description
        description = x.find('p')
        desc = description.contents[0]
        href = postUrl.get('href')
        url = "https://medium.com"+href
        # print(title)
        # print(desc)
        # print(url)
        # print('\n')
        # creating a dictionary
        artArray.append(title)
        artArray.append(desc)
        artArray.append(url)

    # getting articles by test
    title1 = artArray[0]
    desc1 = artArray[1]
    url1 = artArray[2]

    title2 = artArray[3]
    desc2 = artArray[4]
    url2 = artArray[5]

    title3 = artArray[6]
    desc3 = artArray[7]
    url3 = artArray[8]

    title4 = artArray[9]
    desc4 = artArray[10]
    url4 = artArray[11]

    title5 = artArray[12]
    desc5 = artArray[13]
    url5 = artArray[14]

    # returning the articles (tbh : its noob way to return multiple values but i dont know how to do it other way than this)

    mediumArticles = 'Medium Technology Articles 💻 \n'+'\n'+'Article01 : '+title1+'\n\n' + \
        'Description : '+desc1+'\n\n'+'Read Full article at : '+url1+'\n\n' +\
        '--------x--------'+'\n\n'+'Article_02 : '+title2+'\n\n' + \
        'Description : '+desc2+'\n\n'+'Read Full article at : '+url2+'\n\n'\
        '--------x--------'+'\n\n'+'Article_03 : '+title3+'\n\n' + \
        'Description : '+desc3+'\n\n'+'Read Full article at : '+url3+'\n\n'\
        '--------x--------'+'\n\n'+'Article_04 : '+title4+'\n\n' + \
        'Description : '+desc4+'\n\n'+'Read Full article at : '+url4+'\n\n'\
        '--------x--------'+'\n\n'+'Article_05 : '+title5+'\n\n' + \
        'Description : '+desc5+'\n\n'+'Read Full article at : '+url5+'\n\n'

    return (mediumArticles)


# Getting all techcrunch articles
def get_techcrunch():
    url = "https://techcrunch.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    article_titles, article_contents, article_hrefs = [], [], []

    for tag in soup.findAll("div", {"class": "post-block post-block--image post-block--unread"}):
        tag_header = tag.find("a", {"class": "post-block__title__link"})
        tag_content = tag.find("div", {"class": "post-block__content"})

        article_title = tag_header.get_text().strip()
        article_href = tag_header["href"]
        article_content = tag_content.get_text().strip()

        article_titles.append(article_title)
        article_contents.append(article_content)
        article_hrefs.append(article_href)

    all_articles = []
    article_count = int(len(article_titles))

    for i in range(article_count):
        all_articles.append([])

    for i in range(article_count):
        all_articles[i].append(article_titles[i])
        all_articles[i].append(article_contents[i])
        all_articles[i].append(article_hrefs[i])

    # creating a dictionary
    techcrunchArticles = 'Techcrunch Latest Articles 💻 \n'+'\n'+'Article01 : '+''+all_articles[0][0]+'\n\n' + \
        'Description : '+all_articles[0][1]+'\n\n'+'Read Full article at : '+all_articles[0][2]+'\n\n' +\
        '--------x--------'+'\n\n'+'Article_02 : '+all_articles[1][0]+'\n\n' + \
        'Description : '+all_articles[1][1]+'\n\n'+'Read Full article at : '+all_articles[1][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_03 : '+all_articles[2][0]+'\n\n' + \
        'Description : '+all_articles[2][1]+'\n\n'+'Read Full article at : '+all_articles[2][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_04 : '+all_articles[3][0]+'\n\n' + \
        'Description : '+all_articles[3][1]+'\n\n'+'Read Full article at : '+all_articles[3][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_05 : '+all_articles[4][0]+'\n\n' + \
        'Description : '+all_articles[4][1]+'\n\n' + \
        'Read Full article at : '+all_articles[4][2]+'\n\n'

    furtherArticles = 'Techcrunch Further Articles 💻 \n'+'\n'+'Article06 '+''+all_articles[5][0]+'\n\n' + \
        'Description : '+all_articles[5][1]+'\n\n'+'Read Full article at : '+all_articles[5][2]+'\n\n' +\
        '--------x--------'+'\n\n'+'Article_07 : '+all_articles[6][0]+'\n\n' + \
        'Description : '+all_articles[6][1]+'\n\n'+'Read Full article at : '+all_articles[6][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_08 : '+all_articles[7][0]+'\n\n' + \
        'Description : '+all_articles[7][1]+'\n\n'+'Read Full article at : '+all_articles[7][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_09 : '+all_articles[8][0]+'\n\n' + \
        'Description : '+all_articles[8][1]+'\n\n'+'Read Full article at : '+all_articles[8][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_10 : '+all_articles[9][0]+'\n\n' + \
        'Description : '+all_articles[9][1]+'\n\n' + \
        'Read Full article at : '+all_articles[9][2]+'\n\n'

    # only return title and read full article link

    lastArticles = 'Techcrunch earliest Articles 💻 \n' + '\n'+'Article11 : '+''+all_articles[10][0]+'\n\n' + \
        'Read Full article at : '+all_articles[10][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_12 : '+all_articles[11][0]+'\n\n' + \
        'Read Full article at : '+all_articles[11][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_13 : '+all_articles[12][0]+'\n\n' + \
        'Read Full article at : '+all_articles[12][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_14 : '+all_articles[13][0]+'\n\n' + \
        'Read Full article at : '+all_articles[13][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_15 : '+all_articles[14][0]+'\n\n' + \
        'Read Full article at : '+all_articles[14][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_16 : '+all_articles[15][0]+'\n\n' + \
        'Read Full article at : '+all_articles[15][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_17 : '+all_articles[16][0]+'\n\n' + \
        'Read Full article at : '+all_articles[16][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_18 : '+all_articles[17][0]+'\n\n' + \
        'Read Full article at : '+all_articles[17][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_19 : '+all_articles[18][0]+'\n\n' + \
        'Read Full article at : '+all_articles[18][2]+'\n\n'\
        '--------x--------'+'\n\n'+'Article_20 : '+all_articles[19][0]+'\n\n' + \
        'Read Full article at : '+all_articles[19][2]+'\n\n'\

    print("Tech Crunch Articles sent successfully🚀")

    # with open("articles.txt",'w',encoding = 'utf-8') as f:
    #     for i in range(article_count):
    #         if i:
    #             f.write('\n\n\n\n')
    #         for j in all_articles[i]:
    #             f.write(f"{j} \n\n")

    return (techcrunchArticles, furtherArticles, lastArticles)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']+"\n - by "+json_data[0]['a']
    print('Quotes Sent Succesfully 🚀')
    return (quote)
