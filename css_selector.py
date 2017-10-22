import csv
import requests
from bs4 import BeautifulSoup
data_list=[]
site = requests.get('https://stackoverflow.com/');
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')
    questions = content.select('.question-summary')
    for question in questions:
        topic = question.select( '.question-hyperlink')[0].get_text()
        url = question.select( '.question-hyperlink')[0].get('href')
        views = question.select('.views .mini-counts span')[0].get_text()
        answers = question.select('.status .mini-counts span')[0].get_text()
        votes = question.select('.votes .mini-counts span')[0].get_text()
        new_data = {"topic": topic, "url": url, "views": views, "answers":answers, "votes":votes}
        data_list.append(new_data)
    with open ('selector.csv','w') as file:
        writer = csv.DictWriter(file, fieldnames = ["topic", "url", "views", "answers", "votes"], delimiter = ';')
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)
