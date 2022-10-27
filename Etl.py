import requests
from bs4 import BeautifulSoup

def getStatusCode(url):
  response = requests.get(url)
  status = response.status_code
  return status

def getContent(url):
  response = requests.get(url)
  contentHtml = response.content
  return contentHtml

def getAllTitles(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content , "html.parser")
  a = soup.find_all("a")
  return a