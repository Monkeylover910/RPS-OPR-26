import requests
imena=["Luka","Bor","Aleksandar","Alen","Andraž"]
#enumerate= doda index v list (enumerate(imena))
največ=0
for i in imena:
    url= f"https://api.agify.io/?name={i}"
    call=requests.get(url).json()
    st=call["age"]
    if st>največ:
        največ=st
        ime=i
print(ime,največ)
