# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:45:58 2021

@author: Grawiton
"""

import pywikibot
import datetime

#This is a sample list
list = ["Koprzywnica (stacja kolejowa)","Kańczuga (stacja kolejowa)"]
for article in list:
    
    print(article)
    site = pywikibot.Site("pl", "wikipedia")
    page = pywikibot.Page(site, article)
    item = pywikibot.ItemPage.fromPage(page)
    dictionary = item.get()
    try:
        print(dictionary['descriptions']['pl'])
    except:
        print('there is no description')
    #%%
    try:
        if len(dictionary['claims']['P197'])>0:
            print("there is p197")
    except:
        print("there is no p197")
            
    
    text = page.text
    
    
    
    #%%
    
    pop=text[text.find("[[",text.find("poprzedni "))+2:min(text.find("]]",text.find("poprzedni ")),text.find("|",text.find("poprzedni ")))]
    print(pop)
    try:
        pagepop=pywikibot.Page(site,pop)
        itempop=pywikibot.ItemPage.fromPage(pagepop)
        dictpop=itempop.get()
        
        site = pywikibot.Site("wikidata", "wikidata")
        repo = site.data_repository()
        item = pywikibot.ItemPage(repo, str(item)[11:-2])
        claim = pywikibot.Claim(repo, u'P197')
        target = pywikibot.ItemPage(repo, str(itempop)[11:-2])
        claim.setTarget(target)
        item.addClaim(claim, summary=u'Adding claim')
        
        date = datetime.date.today()
        yea = int(date.strftime("%Y"))
        mont=int(date.strftime("%m"))
        da=int(date.strftime("%d"))
        
        statedin = pywikibot.Claim(repo, u'P143')
        itis = pywikibot.ItemPage(repo, "Q1551807")
        statedin.setTarget(itis)
        
        retrieved = pywikibot.Claim(repo, u'P813')
        date = pywikibot.WbTime(year=yea, month=mont, day=da)
        retrieved.setTarget(date)
        
        claim.addSources([statedin, retrieved], summary=u'Adding sources.')
    except:
        print(f"there is no {pop}")
        
    #%%
    
    nast=text[text.find("[[",text.find("następny "))+2:min(text.find("]]",text.find("następny ")),text.find("|",text.find("następny ")))]
    print(nast)
    try:
        pagenast=pywikibot.Page(site,nast)
        itemnast=pywikibot.ItemPage.fromPage(pagenast)
        dictnast=itempop.get()
        
        site = pywikibot.Site("wikidata", "wikidata")
        repo = site.data_repository()
        item = pywikibot.ItemPage(repo, str(item)[11:-2])
        claim = pywikibot.Claim(repo, u'P197')
        target = pywikibot.ItemPage(repo, str(itemnast)[11:-2])
        claim.setTarget(target)
        item.addClaim(claim, summary=u'Adding claim')
        
        date = datetime.date.today()
        yea = int(date.strftime("%Y"))
        mont=int(date.strftime("%m"))
        da=int(date.strftime("%d"))
        
        statedin = pywikibot.Claim(repo, u'P143')
        itis = pywikibot.ItemPage(repo, "Q1551807")
        statedin.setTarget(itis)
        
        retrieved = pywikibot.Claim(repo, u'P813')
        date = pywikibot.WbTime(year=yea, month=mont, day=da)
        retrieved.setTarget(date)
        
        claim.addSources([statedin, retrieved], summary=u'Adding sources.')
    except:
        print(f"there is no {nast}")
    
