import re 
from collections import Counter # Keep track of our term counts
from nltk.corpus import stopwords # Filter out stopwords, such as 'the', 'or', 'and'
import pandas as pd # For converting results to a dataframe and bar chart plots
import csv
import time

def clean_text(text):
    #Cleans stop words, any special characters and any repeated words. Lowers also capital letters
    txt = text
    txt = re.sub("[.,/(){}:]"," ",txt)
    txt = re.sub("[^a-zA-Z0-9-& ]","x",txt)
    text = text.lower().split()
    stop_words = set(stopwords.words("german")) # Filter out any stop words
    text = [w for w in text if not w in stop_words]
    stop_words = set(stopwords.words("english")) # Filter out any stop words
    text = [w for w in text if not w in stop_words]
    text = list(set(text))
    return text 

def read_jobs(file_jobs):
    #read every job description and append it to a main list that will be returned at the end
    job_descriptions = []
    with open(file_jobs, 'rb') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';')
        for row in filereader:
            try:
                raw_data = row[0].split(";")[1].decode('utf-8')
                job_desc = clean_text(raw_data)
                job_descriptions.append(job_desc)
            except:
                pass
    
    return job_descriptions

def analyse_jobs(job_descriptions):
    #Return frequency of each looked up skill
    skills_fq = Counter()
    [skills_fq.update(skill) for skill in job_descriptions]
    prog_lang_dict = Counter({'jQuery':skills_fq['jquery'], 'Python':skills_fq['python'],
                    'Java':skills_fq['java'], 'C++':skills_fq['c++'],
                     'SQL':skills_fq['sql'], 'ASP':skills_fq['asp'],'Javascript':skills_fq['javascript'],
                     'PHP':skills_fq['php'],'CSS':skills_fq['css'],'HTML5':skills_fq['html5'],'PERL':skills_fq['perl'],'CSS3':skills_fq['css3'],
                     'C':skills_fq['c'],'VBA':skills_fq['vba'],'HTML':skills_fq['html'],
                     '.NET':skills_fq['.net'] ,'Bootstrap':skills_fq['bootstrap'],'AJAX':skills_fq['ajax'], 'XML':skills_fq['xml'],'C#':skills_fq['c#'],'Julia':skills_fq['julia'],'NoSQL':skills_fq['nosql'],
                     'AngularJS':skills_fq['angularjs'],'Ruby On Rails':skills_fq['ruby'],'R':skills_fq['r'],'Hadoop':skills_fq['hadoop'],
                     'Spark':skills_fq['spark'],'D3.js':skills_fq['d3.js'] })
    return prog_lang_dict


def plot_data(job_descriptions,target_path):
    Prog_skills = analyse_jobs(job_descriptions)
    skills_data = pd.DataFrame(Prog_skills.items(), columns = ['Skill', 'CountOfPosting']) 
    skills_data.CountOfPosting = (skills_data.CountOfPosting * 100)/len(job_descriptions)
    skills_data.sort(columns = 'CountOfPosting', ascending = False, inplace = True)
    final_plot = skills_data.plot(x = 'Skill', kind = 'bar', legend = None, 
                            title = 'Percentage of IT Job Ads with a Key Skill- B')
        
    final_plot.set_ylabel('Percentage Appearing in Job Ads')
    fig = final_plot.get_figure() # Have to convert the pandas plot object to a matplotlib object
    fig.savefig(target_path +  'tun_plot_berlin.png',bbox_inches='tight')
    return 'Success'

#Put your path here (read from and save figure to)PATH = 
job_descriptions = read_jobs(PATH+FILE)
plot_data(job_descriptions,PATH)
