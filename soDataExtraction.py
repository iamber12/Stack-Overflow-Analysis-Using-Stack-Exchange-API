from stackapi import StackAPI
import csv

SITE = StackAPI('stackoverflow')

# fetch data having tags 'R' and '.net' from 1 June 2021 to 1 Dec 2021
# 'filter' created manually from - https://api.stackexchange.com/docs/search
dotnetTagSearch = SITE.fetch('search', fromdate=1622505600, todate=1638316800, tagged='.net', filter='!)RhXbHRkB6_tPu7aa2kYKD8y')
rTagSearch = SITE.fetch('search', fromdate=1622505600, todate=1638316800, tagged='r', filter='!)RhXbHRkB6_tPu7aa2kYKD8y')
dotnetTagData = []
rTagData = []

# defining fields - 1 identifier + 5 metrics
fields=['Question Id', 'View count', 'Is Answered', 'Answer Count', 'Score', 'Owner Reputation']

# extracting data of 5 metrics
for data in dotnetTagSearch['items']:
    ownerReputation = 0
    if 'reputation' in data['owner']:
        ownerReputation = data['owner']['reputation']
    dotnetTagData.append([data['question_id'],data['view_count'],data['is_answered'],data['answer_count'],data['score'], ownerReputation])
for data in rTagSearch['items']:
    ownerReputation = 0
    if 'reputation' in data['owner']:
        ownerReputation = data['owner']['reputation']
    rTagData.append([data['question_id'],data['view_count'],data['is_answered'],data['answer_count'],data['score'], ownerReputation])

# filenames
dot_net = "./dotNetTagData.csv"
r = "./rTagData.csv"

# generating csv
with open(dot_net, 'w', encoding='UTF8', newline='') as fileToWrite: 
    csvwriter = csv.writer(fileToWrite) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(dotnetTagData)
    
with open(rFileName, 'w', encoding='UTF8', newline='') as fileToWrite: 
    csvwriter = csv.writer(fileToWrite) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rTagData)

