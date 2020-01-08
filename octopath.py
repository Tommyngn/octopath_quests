from flask import Flask
import requests
from bs4 import BeautifulSoup as BS
import csv

app=Flask(__name__)
# app.config['SERVER_NAME'] = 'tommyngn.com'


# csv_file=open('octopath_quest.csv','a')
# csv_writer=csv.writer(csv_file)
#
#
# url='https://octopathtraveler.fandom.com/wiki/Kaia,_Mother_of_Dragons_(I)'
#
# response=requests.get(url)
#
# print(response.status_code)
#
# soup=BS(response.content,'lxml')
#
# span=soup.find_all('span')
#
#
# for pos1, i in enumerate(span):
#     if 'white-space:' in str(i):
#         # print('POSITION::'+str(pos1)+'::',i)
#         list_=str(i).split('" ')
#         for item in list_:c
#             if 'title=' in str(item):
#                 list2=str(item).split('"')
#                 csv_writer.writerow([list2[1],'not complete'])


@app.route('/')
def hello():
    return 'Hello World'

@app.route('/reamaining_quests')
def remaining_quests():

    remain=''

    csv_file=open('octopath_quest_complete.csv','r')
    list_=list(csv.reader(csv_file))
    for pos1, i in enumerate(list_):
        if i[1] == 'not complete':
            remain+=str(i) + '\n'

    return remain


@app.route('/update_quests_complete/<name>')
def update_quest_complete(name):

    name=name.replace('_',' ')

    csv_read=open('octopath_quest_complete.csv','r')
    list_=list(csv.reader(csv_read))

    csv_read.close()

    csv_out=open('octopath_quest_complete.csv','w')
    csv_writer=csv.writer(csv_out)


    for pos1, i in enumerate(list_):
        if i[0] == name:
            csv_writer.writerow([i[0],'complete'])
        else:
            csv_writer.writerow([i[0],i[1]])

    return name


@app.route('/update')
def update():
    csv_out = open('octopath_quest_complete.csv', 'w')
    csv_writer = csv.writer(csv_out)
    csv_read = open('octopath_quest.csv', 'r')
    list_ = list(csv.reader(csv_read))

    for pos1, i in enumerate(list_):
        if pos1<86:
            csv_writer.writerow([i[0],'complete'])
        else:
            csv_writer.writerow([i[0],'not complete'])

    return 'Done'



if __name__ == '__main__':
    app.run()






