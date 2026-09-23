import random
import requests

st=4
url=f"https://opentdb.com/api.php?amount={st}&type=multiple"
call=requests.get(url).json()

for i in range(st):
    prav=call["results"][i]["correct_answer"]
    odgovori=call["results"][i]["incorrect_answers"] + [prav]
    odgovori=random.shuffle(odgovori)

    print(call["results"][i]["question"])

