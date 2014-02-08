"""
Fetch jobs from indeed, find company review(score, 
salary range) from Glassdoor. Short list jobs by companies
those are found on glassdoor with score above 2 (out of 5)
There are some cases where a company is not found on 
glassdoor, hence those jobs get droped from the list. 
Ex: Amazon Corporate LLC. Such cases are just printed.

For details please read README.txt
"""
from indeed import IndeedClient
from glassdoor import get as glass_get
from bs4 import BeautifulSoup
from pprint import pprint
import json

#Indeed.com API Key and query
INDEED_KEY          = 'PUTYOUROWN' 
INDEED_MAX_JOB      = 20
INDEED_SEARCH_FOR   = "Python"
INDEED_JOB_LOC      = "Seattle"
# for more queries refer- https://github.com/indeedlabs/indeed-python

def extract_listings(doc):
    """ Extract from indeed """
    for result in doc['results'] :
        listing_dict = { 
            'in_company': result['company'].strip(),
            'url': result['url'].strip(),
            'title': result['jobtitle'].strip(),
        }   
        yield listing_dict


def indeed_fetch(q=None, l=None, limit=10, userip="1.2.3.4", 
                useragent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"):
    """ Fetch jobs from indeed, userip, useragent parameters are must.
    provided some dummy values"""
    incoming = locals().copy()
    client = IndeedClient(INDEED_KEY)
    search_params = dict(
        [(key, val) for key, val in incoming.items() if val is not None])
    if not search_params:
        raise ValueError("No valid keywords")
    search_response = client.search(**search_params)
    return search_response


def glassdoor_fetch(di):
    """Fetch glassdoor review for the company name 
    posted in indeed.
    """
    comp = str(di['in_company'])
    temp =  glass_get(comp)   
    temp = temp.json()
    comp_info = json.loads(temp)
    if(comp_info.get('error', None)):
        print "%s : Company review not found on glassdoor!\n" %(comp)
        print "---------------------------------------------------------\n"
        di['gd_score']  = None
        di['gd_salary'] = None
    else:
        di['gd_score'] = comp_info.get('satisfaction', None)['score']                
        di['gd_salary'] = comp_info.get('salary', None)[0]['range']
        di['gd_company']= comp_info.get('meta', None)['name']
    return di 

def filter_by_glass_score(di):
    """Filter by glassdoor score"""
    if ((di['gd_score'] == None) or (float(di['gd_score']) < 2.0)):
        return None
    else: 
        return di

if __name__ == '__main__':
    res = indeed_fetch(q=INDEED_SEARCH_FOR, 
                       l=INDEED_JOB_LOC, 
                       limit=INDEED_MAX_JOB)
    for listing in extract_listings(res):
        listing = glassdoor_fetch(listing)
        listing = filter_by_glass_score(listing)
        if listing is not None:
            pprint(listing)
            print "---------------------------------------------------------\n"
