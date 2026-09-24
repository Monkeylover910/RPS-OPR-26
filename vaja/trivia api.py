import random
import requests

st=int(input("Koliko vprašanj hočeš? --> "))
url=f"https://opentdb.com/api.php?amount={st}&type=multiple"
call=requests.get(url).json()

for i in range(st):
    prav=call["results"][i]["correct_answer"]
    narobe=call["results"][i]["incorrect_answers"]
    odgovori=call["results"][i]["incorrect_answers"] + [prav]
    abc=["A","B","C","D"]
    #random.shuffle(odgovori)
    print("*"*80)
    print(call["results"][i]["category"])
    print(call["results"][i]["difficulty"])
    print()
    print(call["results"][i]["question"])
    print("*"*80)
    print(odgovori)
    od=str(input("Kaj je pravilen odgovor?(A,B,C,D) -->  "))
    if abc.index(od)==odgovori.index(prav):
        print("Malo jači")
    else:
        print("Zanč si")
    print("*"*80)
    print()

    

