import csv
from openai import OpenAI
import os

# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = 'your API key'
client = OpenAI()
def check_match_with_gpt(question, ground_truth, predicted):
    # Construct the prompt for GPT-4
    prompt = f"Question: {question}\nGround Truth Answer: {ground_truth}\nPredicted Answer: {predicted}\nDoes the predicted answer match the ground truth? Answer 1 for match and 0 for not match. Use semantic meaning not exact match. Synonyms are also treated as a match, e.g., football and soccer, playground and ground track field, building and rooftop, pond and swimming pool. Do not explain the reason.\n"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                ]
            }
        ],
        max_tokens=100,
    )
    answer = response.choices[0].message.content

    return answer

import json
sumValue=0
correctValue=0
results=[]
f = open('clair_VQAresult.json', 'w')
# 打开 .csv 文件
with open('./VQA_result.csv', mode='r', newline='', encoding='utf-8') as file: # Caption
    csv_reader = csv.reader(file)  # create a CSV reader
    for row in csv_reader:
        image_name=row[0] # Image name
        question=row[2].lower() # Question
        ground_truth=row[3].lower() # GT
        predicted=row[1].lower() # Predict

        print(question)
        if ground_truth in predicted:
            match_result = '1'
        elif ground_truth in ['yes', 'no'] + list(map(str, range(100))):
            match_result = '1' if ground_truth == predicted else '0'
        else:
            match_result = check_match_with_gpt(question, ground_truth, predicted)

        result = {
            "question": question,
            "ground_truth": ground_truth,
            "predicted": predicted,
            "correct": match_result,
        }
        results.append(result)
        f.write(json.dumps(result) + '\n')
        f.flush()
        sumValue += 1
        correctValue+=int(match_result)

print('Overall Accuracy: ',correctValue/sumValue)
