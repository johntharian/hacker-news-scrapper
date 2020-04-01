import requests
from bs4 import BeautifulSoup
import pprint
'''


read the websiteb carefully 
look at the inspect elementn
creafully  look at the tags in the website 


'''
res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')

# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.select('a'))
''' css selector'''

links = soup.select('.storylink')
subtext = soup.select('.subtext')
# links2 = soup2.select('.storylink')
# subtext2 = soup2.select('.subtext')

# mega_links = links+links2
# mega_subtext = subtext+subtext2
''' we are using .subtect and not .score because some 
links have  no score'''
# print(votes[0].get('id'))


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtect):
    hn = []
    for idx, item in enumerate(links):
        '''title=links[idx].getext(), href=links[idx].get('href',None)'''
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})
    return sort_stories_by_votes(hn)


# pprint.pprint(create_custom_hn(mega_links, mega_subtext))
pprint.pprint(create_custom_hn(links,subtext))
