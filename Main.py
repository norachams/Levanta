import json
import random
import requests
import re
from collections import Counter
from dotenv import load_dotenv
import os
import cohere
from twilio.rest import Client


load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN not set")

# Building a function that reads form github to know what questions were already solved and not repeat
def getQuestions():

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

    #and now we want to 
    assigned = random.choice(list(todo)) if todo else None

    return assigned



def generate_message():
    COHERE_TOKEN = os.getenv("COHERE_TOKEN")

    co = cohere.ClientV2(api_key=COHERE_TOKEN)
    if not COHERE_TOKEN:
        raise RuntimeError("Cohere api missing")

    response = co.chat(
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are Levanta, a no-nonsense motivational coach designed to push someone to do their daily LeetCode practice. \nYour job is to send brutally honest, tough-love motivational texts that feel like a slap in the face. \n\nStyle rules:\n- Always 50–150 words long.\n- Bold, sarcastic, and emotionally charged.\n- Use exactly ONE real-life example of a person who grinded their way to success. Never mention more than one person per text.\n- Include at least one motivational quote or hard truth.\n- Add 1–2 emojis for impact \n- Make the reader feel FOMO, guilt, and urgency as if they are falling behind while others succeed.\n- Never be repetitive. Every response must feel unique and punchy.\n- End with a direct call to action: \"Open LeetCode\", \"Solve now\", or \"Do one problem today\" or similar.\n\nYour mission: make the user feel like they’re wasting their life if they don’t open LeetCode right now."
                    }
                ]
            },
            {
                "role": "user",
                "content": [{"type": "text", "text": "Give me a brutal wake-up call to do LeetCode now."}]
            }
        ],
        temperature=1,
        model="command-a-03-2025",
    )

    #text = response.output_text if hasattr(response, "output_text") else str(response)
    text = response.message.content[0].text 
    leetcode_q = getQuestions()
    final_text = text + (f"\n\nToday's problem: {leetcode_q}" if leetcode_q else "\n\nNo pending problems found 🎉")

   

    return final_text

if __name__ == "__main__":
    print(generate_message())

