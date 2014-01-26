******************************************************************
Session:3 Assignments / Maitri Kashyap 
glassdeed.py - Indeed, glassdoor mashup.
*****************************************************************

(*) Description : 

Search jobs from indeed.com, shortlist them by 
the company ratings @Glassdoor.

(*) Pros & Cons   : 

    *) Can instantly get the salary range, company score 
    from glassdoor.
    *) Glassdoor might not have reviews for a company. 
      For now, such cases are just printed to stdout. 

(*) Prerequisites:

    1) Glassdoor API
    This is not an offcial package from glassdoor. 
    So an API key is not required. But I spent a lot of time fixing it! 
    https://pypi.python.org/pypi/glassdoor
    Home Page: http://github.com/hackerlist/glassdoor

    *) pip install glassdoor  - in virtual env.
    *) Then found that gd.py installed wasn't sufficient to find the 
       company when it is not the "only" exact match. 
       - Had to tweak the code to find the closest match instead of returning 
         suggestions without link.  
       - Had to tweak for fetching the right score value for the seconday 
         search.
    *) After installing glassdoor; find gd.py in the path below and 
       replace with the gd.py in this pullrequest. 
       path:./soupenv/lib/python2.7/site-packages/glassdoor/gd.py

    2) Indeed API
    API key required, but code already includes my key. 
    https://github.com/indeedlabs/indeed-python
    
    *) pip install indeed - in virtual env.
    
(*) Source Code :

    Once prerequisites are in place, run glassdeed.
    Searches "Python" jobs(20) in "Seattle" (within 25 miles radius).
    Gets the company score and salary range from glassdoor.
    Filters for score above 2.0(out of 5)
    Printed out to stdout.

    *) python glassdeed.py 

(*) Output example 

    {'gd_company': u'UW Medicine',             -- Best matched company by glassdoor
      'gd_salary': [65000, 88000],             -- Company Salary range by glassdoor
      'gd_score': 3.2,                         -- Comany rating by glassdoor 
      'in_company': u'University of Washington  
                    Medical Center',           -- Company name by Indeed
      'title': u'SOFTWARE ENGINEER',           -- Position by indeed
      'url': u'http://www.indeed.com/viewjob?jk
                =d6cd1efd3e805587&qd=...}      -- Job url
                                                        
(*) In addition, I registered for LinkedIn APIs, and tried out few things.
    They have real good examples to start with. 
    http://nbviewer.ipython.org/github/ptwobrussell/Mining-the-Social-Web-2nd-Edition/blob/master/ipynb/Chapter%203%20-%20Mining%20LinkedIn.ipynb
