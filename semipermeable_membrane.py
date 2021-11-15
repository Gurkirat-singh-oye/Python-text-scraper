import requests
from requests_html import HTMLSession
import lxml

URL = []

def scoping(url):
    
    try:
        page = HTMLSession().get(str(url))
    except ValueError:
        print ("ValueError: Not a valid url.")
        page = "--:--"
        print ("Moving On...")
        return None
    return (page)

def membrane(httpctx):
    htmlctx = lxml.html.fromstring(httpctx.content)
    tmptxt = ""
    tmptxt = (htmlctx.xpath('.//div[@class="main-content single-article-content"]//text()'))
    tmptxt = "".join(tmptxt[:len(tmptxt)])
    tmptxt = tmptxt.replace('[\'','')
    tmptxt = tmptxt.replace('\']','')
    tmptxt = tmptxt.replace('\n',' ')
    tmptxt = tmptxt.replace(' ', '')
    return tmptxt.replace("  ", "")