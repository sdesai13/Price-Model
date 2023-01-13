#!/usr/bin/python

import lxml
from bs4 import BeautifulSoup
import bs4
import requests
import time
import selenium
import csv



url = "https://www.zillow.com/toronto-on/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.77051922962714%2C%22east%22%3A-78.98225018665839%2C%22south%22%3A43.57640738664757%2C%22north%22%3A43.83947561739885%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# get your headers from http://myhttpheader.com

res = requests.get(url, headers={})


url2 = "https://www.zillow.com/toronto-on/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.77051922962714%2C%22east%22%3A-78.98225018665839%2C%22south%22%3A43.393568616256196%2C%22north%22%3A44.020961305917474%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url3 = "https://www.zillow.com/toronto-on/3_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A3%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.77051922962714%2C%22east%22%3A-78.98225018665839%2C%22south%22%3A43.393568616256196%2C%22north%22%3A44.020961305917474%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url4 = "https://www.zillow.com/toronto-on/4_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A4%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url5 = "https://www.zillow.com/toronto-on/5_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A5%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url6 = "https://www.zillow.com/toronto-on/6_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A6%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url7 = "https://www.zillow.com/toronto-on/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A7%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url8 = "https://www.zillow.com/toronto-on/8_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A8%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url9 = "https://www.zillow.com/toronto-on/9_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A9%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url10 = "https://www.zillow.com/toronto-on/10_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A10%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url11 = "https://www.zillow.com/toronto-on/11_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A11%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url12 = "https://www.zillow.com/toronto-on/12_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A12%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url13 = "https://www.zillow.com/toronto-on/13_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A13%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url14 = "https://www.zillow.com/toronto-on/14_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A14%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url15 = "https://www.zillow.com/toronto-on/15_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A15%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url16 = "https://www.zillow.com/toronto-on/16_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A16%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url17 = "https://www.zillow.com/toronto-on/17_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A17%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url18 = "https://www.zillow.com/toronto-on/18_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A18%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url19 = "https://www.zillow.com/toronto-on/19_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A19%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url20 = "https://www.zillow.com/toronto-on/20_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A20%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url21 = "https://www.zillow.com/brampton-on/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Brampton%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.99646320237221%2C%22east%22%3A-79.52267780198159%2C%22south%22%3A43.55067614242394%2C%22north%22%3A43.899018514819204%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
url22 = "https://www.zillow.com/brampton-on/2_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Brampton%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.99646320237221%2C%22east%22%3A-79.52267780198159%2C%22south%22%3A43.55067614242394%2C%22north%22%3A43.899018514819204%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D"
url23 = "https://www.zillow.com/brampton-on/3_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Brampton%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.99646320237221%2C%22east%22%3A-79.52267780198159%2C%22south%22%3A43.55067614242394%2C%22north%22%3A43.899018514819204%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%22currentPage%22%3A3%7D%7D"
url24 = "https://www.zillow.com/mississauga-on/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.90349887633437%2C%22east%22%3A-79.42971347594374%2C%22south%22%3A43.431493613186845%2C%22north%22%3A43.78052627192224%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792679%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
url25 = "https://www.zillow.com/mississauga-on/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.90349887633437%2C%22east%22%3A-79.42971347594374%2C%22south%22%3A43.431493613186845%2C%22north%22%3A43.78052627192224%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792679%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
url26 = "https://www.zillow.com/brampton-on/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A43.899018236772804%2C%22east%22%3A-79.52267779980468%2C%22south%22%3A43.550675862756%2C%22west%22%3A-79.99646320019531%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
url27 = "https://www.zillow.com/brampton-on/2_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A43.899018236772804%2C%22east%22%3A-79.52267779980468%2C%22south%22%3A43.550675862756%2C%22west%22%3A-79.99646320019531%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D"
url28 = "https://www.zillow.com/brampton-on/3_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A43.899018236772804%2C%22east%22%3A-79.52267779980468%2C%22south%22%3A43.550675862756%2C%22west%22%3A-79.99646320019531%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A3%7D%7D"
url29 = "https://www.zillow.com/brampton-on/6_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A43.899018236772804%2C%22east%22%3A-79.52267779980468%2C%22south%22%3A43.550675862756%2C%22west%22%3A-79.99646320019531%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A6%7D%7D"
url30 = "https://www.zillow.com/brampton-on/7_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A43.899018236772804%2C%22east%22%3A-79.52267779980468%2C%22south%22%3A43.550675862756%2C%22west%22%3A-79.99646320019531%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A7%7D%7D"
url31 = "https://www.zillow.com/brampton-on/8_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A43.899018236772804%2C%22east%22%3A-79.52267779980468%2C%22south%22%3A43.550675862756%2C%22west%22%3A-79.99646320019531%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A8%7D%7D"
url32 = "https://www.zillow.com/vaughan-on/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A44.010714642257%2C%22east%22%3A-79.3289007998047%2C%22south%22%3A43.66302434100206%2C%22west%22%3A-79.80268620019532%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792841%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
url33 = "https://www.zillow.com/vaughan-on/2_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A44.010714642257%2C%22east%22%3A-79.3289007998047%2C%22south%22%3A43.66302434100206%2C%22west%22%3A-79.80268620019532%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792841%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D"
url34 = "https://www.zillow.com/vaughan-on/3_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A44.010714642257%2C%22east%22%3A-79.3289007998047%2C%22south%22%3A43.66302434100206%2C%22west%22%3A-79.80268620019532%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792841%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A3%7D%7D"
url35 = "https://www.zillow.com/vaughan-on/4_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A44.010714642257%2C%22east%22%3A-79.3289007998047%2C%22south%22%3A43.66302434100206%2C%22west%22%3A-79.80268620019532%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792841%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A4%7D%7D"
url36 = "https://www.zillow.com/vaughan-on/5_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A44.010714642257%2C%22east%22%3A-79.3289007998047%2C%22south%22%3A43.66302434100206%2C%22west%22%3A-79.80268620019532%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792841%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A5%7D%7D"
url37 = "https://www.zillow.com/vaughan-on/6_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22north%22%3A44.010714642257%2C%22east%22%3A-79.3289007998047%2C%22south%22%3A43.66302434100206%2C%22west%22%3A-79.80268620019532%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792841%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%22currentPage%22%3A6%7D%7D"


urllist = [url, url2, url3, url4, url5, url6, url7, url8, url9, url10, url11, url12, url13,
           url14, url15, url16, url17, url18, url19, url20, url21, url22, url23, url24, url25, url26, url27, url28, url29, url30, url31, url32, url33, url34,
           url35, url36, url37]
testpricelist = []
testaddylist = []
bed_ba = []

for url in urllist:

    res = requests.get(url, headers={})

    soup = BeautifulSoup(res.text, "lxml")

    divresult = soup.find_all('div', class_='StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0 wgiFT')
    priceresult = [soup.get_text() for soup in divresult]


    addyresult = soup.select("address")
    beds = soup.find_all('ul', class_='StyledPropertyCardHomeDetailsList-c11n-8-81-1__sc-1xvdaej-0 cBiTXE')

    bed_b3 = [house.get_text() for house in beds]

    bed_ba.extend(bed_b3)








    for houses in priceresult:

            num = houses[2:]
            finalnum = (num.replace(",", ""))
            finallnum = (finalnum.replace("+", ""))
            ## print(finalnum)
            testnum = 0;
            try:
              testnum =  float(finallnum)
            except ValueError:

                testpricelist.append(0)
                continue
            testpricelist.append(testnum)

    for addy in addyresult:
        testaddylist.append(addy.text)




citylist = []

for address in testaddylist:
    if(address.find("Toronto") != -1):
        citylist.append("Toronto")
    elif (address.find("Mississauga") != -1):
        citylist.append("Mississauga")
    elif (address.find("Brampton") != -1):
        citylist.append("Brampton")
    elif (address.find("Vaughan") != -1):
        citylist.append("Vaughan")
    else:
        citylist.append("N/A")

postList = []

for address in testaddylist:
    num = address.find("ON")
    if (num != -1):
      postList.append(address[num+3:num+6])

    else:
        postList.append("N/A")


bedslist = []
bathlist = []

for houses in bed_ba:
    if houses.find("ba") == -1 or houses.find("bds") == 1:
      bedslist.append("n/a")
    else:
        try:
            testnum = (float(houses[0]))
            bedslist.append(testnum)
        except ValueError:
            bedslist.append("n/a")

for houses in bed_ba:
    if houses.find("ba") == -1 or houses.find("bds") == 1:
      bathlist.append("n/a")
    else:
        try:
            testnum = (float(houses[4]))
            bathlist.append(testnum)
        except ValueError:
            try:
                testnum = (float(houses[5]))
                bathlist.append(testnum)
            except ValueError:
                bathlist.append("n/a")


datalist = list(zip(testpricelist,citylist,bedslist,bathlist))




item_length = len(datalist[0])

# make 2 csv's so we can  transpose the rows to columns

with open('data.csv', 'w') as test_file:
  file_writer = csv.writer(test_file)
  for i in range(item_length):
    file_writer.writerow([x[i] for x in datalist])

import pandas as pd
pd.read_csv('data.csv', header=None).T.to_csv('data2.csv', header=False, index=False)

