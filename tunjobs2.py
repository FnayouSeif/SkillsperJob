# -*- coding: utf-8 -*-
from lxml import html
import requests
import csv
from bs4 import BeautifulSoup
import re


def write_ln(line_str):
    csvfile = "C:/Users/msf/Desktop/itjobs/Tun_Jobs.csv"
    with open(csvfile, "a") as output:
        writer = csv.writer(output,delimiter =";", lineterminator='\n',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([line_str])
    output.close()

def get_text(job_url):
    page = requests.get(job_url)
    soup_obj = BeautifulSoup(page.content,"lxml") 
    for script in soup_obj(["script", "style"]):
        script.extract() # Remove these two elements from the BS4 object
    text = soup_obj.get_text()
    #text = re.sub("[^a-zA-Z.+3#5,/\;() ]","X", text)
    #text = re.sub("[^a-zA-Z.+3#5 ]"," ", text)
    text = ' '.join(text.split())
    return text

def get_stream(url):
    #Get the html stream for jobs page
    page = requests.get(url)
    #page.encoding = 'utf-8'
    xml_stream = html.fromstring(page.content) 
    return xml_stream 


def get_links(xml_stream):
    #get the HREF links for every job post, puts them in a list
    links = xml_stream.xpath('//div/div/div/div[@class="detail"]/a/@href')
    return links
#Main Proc 
ID = 1
num = 0
for pge in xrange(1,37):
    print 'Starting Page : ' + str(pge)
    #Simply, for each page, get the links and for each link, naviguate to job description and get information
    url = 'http://tanitjobs.com/offres-emploi-par-categorie/Informatique/?searchId=1462663119.0465&action=search&page='+str(pge)+'&listings_per_page=20&view=list'
    xml_stream = get_stream(url)
    links_list = get_links(xml_stream)
    #now processing for each link 
    for job_url in links_list:
        record = []
        record.append(str(ID))
        try:
            job_info = get_text(job_url)    
            record.append(job_info)
            print 'Successfully extract Job ' + str(ID) + 'char length = ' + str(len(job_info))
        except:
            print 'Failed at extracting Job ' + str(ID)

        ID = ID + 1
        num = num + 1

        write_ln(str(ID)+ ';' +job_info.encode('utf-8'))
    
    
    

