from bs4 import BeautifulSoup
import requests
import time

# with open('home.html','r') as html_file:
#     content=html_file.read()
#    # print(content)

#     soup=BeautifulSoup(content,'lxml')#lxml is a parser parameter
#     course_cards=soup.find_all('div',class_='card')
#     for course in course_cards:
#         course_names=course.h5.text
#         course_price=course.a.text.split()[-1]
#         print(f'{course_names} costs {course_price}')

# print('Enter skill that not familiar with')
# unfamiliar_skill=input('>')
# print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
  html_text= requests.get('https://www.flipkart.com/search?q=mobiles+under+15000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+15000%7CMobiles&requestId=9a7cbed4-301a-400c-8e6a-cf89a4d46fab&as-searchtext=mobiles%20under%20').text
  
#   soup=BeautifulSoup('html_text','lxml')
#   jobs=soup.find_all('div',class_='col col-7-12')
#   # if job:
#   #   text=job.text
#   #   print(text)
#   for index,job in enumerate(jobs):
#     published_date=job.find('h3',class_='').text
#     if 'few' in published_date:
#        company_name=job.find('h3',class_='').text #get_text(strip=True)
#        skills=job.find('h3',class_='').text.replace(' ','')
#        more_info=job.header.h2.a['href']  
#        if unfamiliar_skill not in skills:   
#           with open('posts/{index}.txt','w') as f:           
#             f.write(f"company Name:{company_name.strip()}\n")  #strip() removes spaces
#             f.write(f"Required skills:{skills}\n")
#             f.write(f"More Information:{more_info}\n")
     
# if __name__=='__main__':
#    while True:
#       find_jobs()
#       time_wait=10
#       print(f'Waiting {time_wait} minute...')
#       time.sleep(time_wait*60)
   
   