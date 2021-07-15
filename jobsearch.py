# Author: Eoghan O'Connor
#
#
# This code searches for job postings on indeed 
#
# Setup: To use 1) Install requests (pip install requests)
#		 	   2) Install beautifulSoup (pip install beautifulsoup)
#			   3) Change headers for your user agent (i.e. type my user agent into google)
#
#
#
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


#INDICATE JOBS AND LOCATIONS
jobs=['machine learning','automation','software',]
locations=['Cork','limerick','Dublin']#Leave blank if particular place of interest e.g '




class indeed:
	def __init__(self,jobs,locations):
		self.job=jobs
		self.location-locations
	def extract(page,job,location):
		
		job=job.replace(' ','+')
		headers = {'User=Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
		url=f'https://ie.indeed.com/jobs?q={job}&l={location}&start={page}'
		r=requests.get(url, headers)
		soup= BeautifulSoup(r.content, 'html.parser')
		return soup


	def transform(soup):
		
		divs= soup.find_all('a', class_="tapItem")

		for post in divs:
			try:
				link='https://ie.indeed.com/'+post.get('href')
				title=post.find('h2',class_=('jobTitle')).text
				company=post.find('span', class_=('companyName')).text
				location=post.find('div',class_=('companyLocation')).text
				salary= post.find('span', class_=('salary-snippet')).text
				
				

			except:
				salary=''
				
			job={
			'title': title,
			'company': company,
			'salary': salary,
			'location': location,
			'Link': link	
			}
			
			
			joblist.append(job)
			
		return


class jobsie:
	def __init__(self,jobs,locations):
		self.job=jobs
		self.location=locations


	def extract(job,location):
		job=job.replace(' ','-')
		if location !='':
			loc='-in-'+location
		else:
			loc=''

		headers = {'User=Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
		url=f'https://www.jobs.ie/{job}-jobs{loc}'
		r=requests.get(url, headers)
		soup= BeautifulSoup(r.content, 'html.parser')
		return soup


	def transform(soup):
		
		divs= soup.find_all('div', class_="job-details-header")
		print(f"found {len(divs)} related posts on jobs.ie")
		for post in divs:
			try:
				
				title=post.find('h2').text
				company=post.find('text', class_=('company-title-name')).text
				location=post.find('dd',class_=('fa-map-marker')).text
				salary= post.find('dd', class_=('fa-eur')).text
				hyperlink=post.find('a',{'title':title})
				link=hyperlink.get('href')
			except:
				link='no link'



			job={
			'title': title,
			'company': company,
			'salary': salary,
			'location': location,
			'Link': link	
			}
			
			joblist.append(job)
			
		return


joblist=[]

if len(jobs):
	pass
else:
	print("Indicate a job")
	exit(0)
for job in jobs:
	print(f'searching for {job}  on indeed.ie')
	for location in locations:
		if location !='':
			print(f'in {location} \n \n')
		for i in range(0,50,10):
			# time.sleep(1)
			print(f'found {int(i+10*1.5)} related posts on indeed')
			c = indeed.extract(i,job,location)
			indeed.transform(c) 
		print('\n')
		print(f'searching for {job} roles on jobs.ie')
		if location !='':
			print(f'in {location} \n \n')
		c = jobsie.extract(job,location)
		jobsie.transform(c) 
		print('\n')




df=pd.DataFrame(joblist)
print(df.head())




try:
	df.to_csv('jobs.csv')
	print('saved locally in excel file called jobs.csv')
except:
	print("CANT SAVE : \n Close open excel sheet")





