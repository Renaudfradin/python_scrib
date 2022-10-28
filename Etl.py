from logging import _srcfile
from urllib import response
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
  titles = soup.find_all("a", class_="gem-c-document-list__item-title")
  return titles

def getImgOneArctile(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content , "html.parser")
  imgs = soup.find_all("img", class_="app-c-figure__image")
  return imgs