import whois
import requests
from bs4 import BeautifulSoup
def domainInfo(domain):
    domaininfo=whois.whois(domain)
    return domaininfo
def publicProfile(url):
    headers={'User-Agent':'Mozilla/5.0'}
    response =requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    profileinfo={}
    profileinfo['name']=soup.find('span',{'class': 'name'}).text
    profileinfo['email']=soup.find('a',{'class': 'email'}).text
    profileinfo['phone']=soup.find('span',{'class':'phone'}).text
    return profileinfo
#how to use this 
domain=input('enter the domain of the target')
url=input('enter url of the target')
domaininfo=domainInfo(domain)
print(f"domain info : {domaininfo}")
profileinfo=publicProfile(url)
print(f"profile info :{profileinfo}")

