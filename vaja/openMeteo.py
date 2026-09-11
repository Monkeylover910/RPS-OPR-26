#izpiši temp za 7 dni
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
max_min(46.2389,14.3556)
