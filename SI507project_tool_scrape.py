from bs4 import BeautifulSoup
import requests, json
from advanced_expiry_caching import Cache
import re


FILENAME = "park_cache.json"
program_cache = Cache(FILENAME)

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def parse_parks():
    '''
    1. cache the content from www.nps.gov
    '''
    for i in range(len(states)):
        eachState = states[i]
        url = "https://www.nps.gov/state/" + eachState + "/index.htm"

        # check if data from this url already exists in cache, if not request.get, then put in cache
        data = program_cache.get(url)
        if not data:
            data = requests.get(url).text
            program_cache.set(url, data, expire_in_days=10)

    '''
    2.parse the cached data in park_cache.json
    '''
    # access the html stored for each state's URL
    urlLst = list(program_cache.cache_diction.values())

    parkInfoLst = []

    parkNameLst = []
    parkTypeLst = []
    parkDesLst = []
    parkStatesLst = []

    for i in range(len(urlLst)):
        soup = BeautifulSoup(urlLst[i]['values'],'html.parser')
        # print(soup.prettify())

        parks = soup.find('ul', id='list_parks').findAll('li', recursive=False)

        for eachPark in parks:
            # Name of the site
            try:
                parkName = eachPark.h3.a.text
                parkNameLst.append(parkName)
            except Exception as e:
                parkName = None

            # type of the site
            try:
                parkType = eachPark.h2.text
                parkTypeLst.append(parkType)
            except Exception as e:
                parkType = None

            # Description of the site
            try:
                parkDes = eachPark.p.text.strip()
                parkDesLst.append(parkDes)
            except Exception as e:
                parkDes = None

            # Locations of the site
            try:
                parkLoc = eachPark.h4.text
                locSplit=re.split('\s+|,',parkLoc)
                stateLst = []
                for s in locSplit:
                    if s.strip().isupper() and len(s.strip())==2:
                        st=s.strip()
                        stateLst.append(st)
                    else:
                        pass
                parkStatesLst.append(stateLst)

            except Exception as e:
                parkLoc = None
                parkState = None

    parkInfoLst.append(parkNameLst)
    parkInfoLst.append(parkTypeLst)
    parkInfoLst.append(parkDesLst)
    parkInfoLst.append(parkStatesLst)

    return parkInfoLst
if __name__ == '__main__':
    parse_parks()
