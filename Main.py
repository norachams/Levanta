import json
import requests
import re
from collections import Counter
from dotenv import load_dotenv
import os


load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN not set")

# Building a function that reads form github to know what questions were already solved and not repeat
def ignoreSolvedQs():

    #getting github repo 
    URL = "https://api.github.com/repos/norachams/leetcode/contents"

    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

    responses = requests.get(URL, headers=headers)
    files = responses.json()
    
    #this part is reading solved questions from my github repo and saving it in set called completed
    completed = set()

    for file in files:
        if file['type'] == 'dir':
            sub_url = file['url']
            sub_response = requests.get(sub_url, headers=headers)
            sub_files = sub_response.json()
        for subfile in sub_files:
            if subfile['name'].endswith('.py'):
                    raw_name = file['name']
                    clean_name = re.sub(r'^\d+\s*', '', raw_name) 
                    folder_title = clean_name.replace("-", " ").title()
                    updated_title = folder_title.lower()
                    completed.add(updated_title[1:] if updated_title.startswith(' ') else updated_title)
            

    #now we want to just look at questions that are not in completed file and take from those 
    todo = set()
    
    with open('NeetcodeQ.json', 'r') as file:
        data = json.load(file)

    count = 0 
    
    for q in data:
        question = q.get("title")
        nquestion = question.lower()
        if nquestion not in completed:
            todo.add(nquestion)
        count+=1

    #so now all questions that are pending to be done are in the set 'todo'

solved = ignoreSolvedQs()








