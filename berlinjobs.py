from lxml import html
import requests
import csv
from bs4 import BeautifulSoup
import re


def write_ln(line_str):
    csvfile = "C:/Users/msf/Desktop/itjobs/Berlin_Jobs.csv"
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

def get_links(url):
    #Returns a list that containts each job URL
    base_url = 'http://de.indeed.com'
    page = requests.get(url)
    stream = html.fromstring(page.content)
    links_temp = stream.xpath('//td[@id = "resultsCol"]/div[@class="  row  result"]/h2/a/@href')
    links = []

    for link in links_temp:
        link = base_url + link
        links.append(link)
    return links

#Main Proc 
ID = 1
num = 0
for pge in xrange(1,85):
    print 'Starting Page : ' + str(pge)
    #Simply, for each page, get the links and for each link, naviguate to job description and get information
    search_page = 'http://de.indeed.com/Jobs?q=software+engineering&l=Berlin&start=' + str(pge*10)
    links_list = get_links(search_page)
    #now processing for each link 
    for job_url in links_list:
        record = []
        record.append(str(ID))
        try:
            job_info = get_text(job_url)    
            record.append(job_info.encode('utf-8'))
            print 'Successfully extract Job ' + str(ID) + ' CHAR length = ' + str(len(job_info))
        except:
            print 'Failed at extracting Job ' + str(ID)

        ID = ID + 1
        num = num + 1

        write_ln(str(ID)+ ';' +job_info.encode('utf-8'))
    
    
    

