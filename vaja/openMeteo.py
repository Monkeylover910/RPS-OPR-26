#izpiši temp za 7 dni
#https://hackmd.io/@lukac/api1
import requests
#def tedn_temp(lat,lon):

    #base_url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max"


    #call=requests.get(base_url).json()
    #print(call["daily"]["temperature_2m_max"])

#tedn_temp(46.2389,14.3556)

#izpiši največjo/najmanjšo
def max_min(la,lo):

    url=f"https://api.open-meteo.com/v1/forecast?latitude={la}&longitude={lo}&daily=temperature_2m_max,temperature_2m_min"
    call=requests.get(url).json()
    for i in range(7):
        print(f"{call["daily"]["temperature_2m_max"][i]}(max) - {call["daily"]["temperature_2m_min"][i]}(min) - {call["daily"]["time"][i]}(dan)")
#max_min(46.2389,14.3556)


def razlika(lan,lon):
    url=f"https://api.open-meteo.com/v1/forecast?latitude={lan}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min"
    call=requests.get(url).json()
    najvec=0
    trenutno=0
    index=0
    temp_max=call["daily"]["temperature_2m_max"]
    temp_min=call["daily"]["temperature_2m_min"]
    for i in range(len(temp_min)):
        trenutno=temp_max[i]-temp_min[i]
        if trenutno>najvec:
            najvec=trenutno
            index=i
    print(call["daily"]["time"][index],najvec)


#razlika(46.2389,14.3556)

def temp2(lat,lon):
    base_url="https://api.open-meteo.com/v1/forecast?"
    parms={"latitude":lat,"longitude":lon, "daily":"temperature_2m_max,temperature_2m_min"}
    call=requests.get(base_url, params=parms)
    json=call.json()
    return json["daily"]["temperature_2m_max"]

mesta = [("Ljubljana", 46.05108, 14.50513),
("Maribor", 46.55583, 15.64593),
("Kranj", 46.23887, 14.35561),
("Celje", 46.23092, 15.26044),
("Koper",45.54820, 13.72963)]

max_temp=0
mes=""
temp_min=100
ms=""

#for c in mesta:
    #print(temp2(c[1],c[2]),c[0])
for c in mesta:
    if max(temp2(c[1],c[2]))>max_temp:
        max_temp=max(temp2(c[1],c[2]))
        mes=c[0] 

for s in mesta:
    if min(temp2(s[1],s[2]))<temp_min:
        temp_min=min(temp2(s[1],s[2]))
        ms=s[0]


        
print(max_temp, mes)
print(temp_min, ms)

    

