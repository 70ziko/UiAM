from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
import time
from datetime import datetime
from .forms import search_city

# Create your views here.



def index(request):


    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = search_city(request.POST)
    else:
        form = search_city()

    cityname = 'Wroclaw'
    PARAMS = {'q': cityname, 'units': 'metric'}
    try:
        response=requests.get(url='https://api.waqi.info/feed/here/?token=840733e07b0dd7eaafa5453a8dce5e1ff715e43e')
        x = response.json()

        x['data']['aqi']


    except:
        print('nie ma takiego miasta')
    URL = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=3b02ead1885113bcf888c7e1fb750c2e'

    try:

        x2 = requests.get(url=URL, params=PARAMS)
        r = x2.json()
        r['list'][0]['dt_txt']
    except:
        print('nie ma takiego miasta')



    time_clokc = '15:00:00'
    next_day = []
    next_day_temperature = []

    fell_like = []
    icon = []


    for k in range(5):
        i = 0
        if not next_day:
            if str(datetime.now().date())[8:10][0] == '0':
                den = int(str(datetime.now().date())[8:10][1])

            else:

                den = int(str(datetime.now().date())[8:10])
                print('Сегодня день: ' + str(den))
        else:
            if str(next_day[-1][8:10][0]) == '0':
                den = int(str(next_day[-1][8:10][1]))

            else:

                den = int(str(next_day[-1][8:10]))

        year = int(str(datetime.now().date())[0:4])
        month = int(str(datetime.now().date())[5:7])
        print('Сегодня год: ' + str(year))
        print('Сегодня месяц: ' + str(month ))
        den += 1
        date = str(year) + "-" +"0"+ str(month) + "-" + str(den)
        print("дата"+date)
        try:
            valid_date = time.strptime(date, '%Y-%m-%d')
            print(valid_date)
        except ValueError:
            den = 1
            month += 1
            date = str(year) + "-" + str(month) + "-" + str(den)
            try:
                valid_date = time.strptime(date, '%Y-%m-%d')

            except ValueError:
                den = 1
                month = 1
                year += 1
                date = str(year) + "-" + str(month) + "-" + str(den)
                try:
                    valid_date = time.strptime(date, '%Y-%m-%d')

                except ValueError:
                    print('gg')

        try:
            i=0
            while r['list'][i]['dt_txt'] != str(str(year) + '-' + str(month) + '-' + '0' + str(den) + ' ' + time_clokc):

                i += 1
                print(i)


        except:
            try:
                i=0
                while r['list'][i]['dt_txt'] != str(str(year) + '-' +"0"+ str(month) + '-'  + str(den) + ' ' + time_clokc):

                    i += 1




            except:
                try:
                    i = 0
                    while r['list'][i]['dt_txt'] != str(str(year) + '-'+"0" + str(month) + '-' + str(den) + ' ' + '06:00:00'):
                        i += 1

                except:
                    i = 0
                    while r['list'][i]['dt_txt'] != str(str(year) + '-' + str(month) + '-' + '0' + str(den) + ' ' + '06:00:00'):
                        i += 1




        next_day.append(r['list'][i]['dt_txt'][:-8])
        next_day_temperature.append(r['list'][i]['main']['temp'])
        icon.append(r['list'][i]['weather'][0]['icon'])


    icon.append(r['list'][0]['weather'][0]['icon'])
    try:
        aqi= x['data']['aqi']
    except:
        aqi= 'Nie ma informacji'
    try:
        co= x['data']['iaqi']['co']['v']
    except:
        co= 'Nie ma informacji'
    try:
       no2= x['data']['iaqi']['no2']['v']
    except:
        no2= 'Nie ma informacji'
    try:
       o3= x['data']['iaqi']['o3']['v']
    except:
        o3= 'Nie ma informacji'
    try:
       pm10= x['data']['iaqi']['pm10']['v']
    except:
        pm10= 'Nie ma informacji'
    try:
       pm25=  x['data']['iaqi']['pm25']['v']
    except:
        pm25= 'Nie ma informacji'
    try:
       so2=  x['data']['iaqi']['so2']['v']
    except:
        so2= 'Nie ma informacji'
    try:
        temp = r['list'][0]['main']['temp']

    except:
        try:
            temp = x['data']['iaqi']['t']['v']
        except:

            temp= 'Nie ma informacji'
    try:
        local=x['data']['city']['name']
        print(x)
    except:
        local=''
    try:
        lan=x['data']['city']['geo'][0]
        log=x['data']['city']['geo'][1]

    except:
        lan = 0
        log =0
    try:
        link=x['data']['attributions'][0]['url']
    except:
        link='none'
    try:
        name=x['data']['attributions'][1]['name']
    except:
        name = 'none'
    weather = {
        'city' : 'Wroclaw',
        'local': local,
        'aqi':aqi,
        'time': str(datetime.now().date()),
        'aqi_co':co ,
        'aqi_no2':no2 ,
        'aqi_o3': o3,
        'aqi_pm10':pm10 ,
        'aqi_pm25':pm25,
        'aqi_so2': so2,
        'aqi_t': temp,
        'feels_like': fell_like,
        'icon': icon[5],
        'icon1': icon[0],
        'icon2': icon[1],
        'icon3': icon[2],
        'icon4': icon[3],
        'icon5': icon[4],
        'next_day1': next_day[0],
        'next_day2': next_day[1],
        'next_day3': next_day[2],
        'next_day4': next_day[3],
        'next_day5': next_day[4],
        'next_day_temperature1': next_day_temperature[0],
        'next_day_temperature2': next_day_temperature[1],
        'next_day_temperature3': next_day_temperature[2],
        'next_day_temperature4': next_day_temperature[3],
        'next_day_temperature5': next_day_temperature[4],
        'form':form,
        'description': r['list'][0]['weather'][0]['description'],
        'log': log,
        'lan': lan,
        'name': name,
        'link': link,
    }
    context={'weather': weather}
    return render(request, 'weather/index.html',context)


def about(request):
    return render(request, 'weather/about.html')

def index2(request):
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = search_city(request.POST)
    else:
        form = search_city()

    cityname = request.POST['search']
    PARAMS = {'q': cityname, 'units': 'metric'}
    try:
        response=requests.get(url='https://api.waqi.info/feed/'+cityname+'/?token=840733e07b0dd7eaafa5453a8dce5e1ff715e43e')
        x = response.json()
        x['data']['aqi']
    except:
        print('nie ma takiego miasta')
    URL = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=3b02ead1885113bcf888c7e1fb750c2e'

    try:

        x2 = requests.get(url=URL, params=PARAMS)
        r = x2.json()
        r['list'][0]['dt_txt']
    except:
        print('nie ma takiego miasta')




    time_clokc = '15:00:00'
    next_day = []
    next_day_temperature = []

    fell_like = []
    icon = []


    for k in range(5):
        i = 0
        if not next_day:
            if str(datetime.now().date())[8:10][0] == '0':
                den = int(str(datetime.now().date())[8:10][1])
                print(str(datetime.now().date())[8:10][0])
            else:
                print('ту десятое число')
                den = int(str(datetime.now().date())[8:10])
        else:
            if str(next_day[-1][8:10][0]) == '0':
                den = int(str(next_day[-1][8:10][1]))

            else:

                den = int(str(next_day[-1][8:10]))

        year = int(str(datetime.now().date())[0:4])
        month = int(str(datetime.now().date())[5:7])

        den += 1
        date = str(year) + "-" + str(month) + "-" + str(den)
        try:
            valid_date = time.strptime(date, '%Y-%m-%d')

        except ValueError:
            den = 1
            month += 1
            date = str(year) + "-" + str(month) + "-" + str(den)
            try:
                valid_date = time.strptime(date, '%Y-%m-%d')

            except ValueError:
                den = 1
                month = 1
                year += 1
                date = str(year) + "-" + str(month) + "-" + str(den)
                try:
                    valid_date = time.strptime(date, '%Y-%m-%d')

                except ValueError:
                    print('gg')

        try:
            i=0
            while r['list'][i]['dt_txt'] != str(str(year) + '-' + str(month) + '-' + '0' + str(den) + ' ' + time_clokc):
                i += 1



        except:
            try:
                i=0
                while r['list'][i]['dt_txt'] != str(str(year) + '-' +"0"+ str(month) + '-'  + str(den) + ' ' + time_clokc):
                    i += 1


            except:
                try:
                    i = 0
                    while r['list'][i]['dt_txt'] != str(str(year) + '-' +'0'+ str(month) + '-' + str(den-1) + ' ' + '06:00:00'):
                        i += 1


                except:
                    i = 0
                    while r['list'][i]['dt_txt'] != str(str(year) + '-' + str(month) + '-' + '0' + str(den-1) + ' ' + '06:00:00'):
                        i += 1





        next_day.append(r['list'][i]['dt_txt'][:-8])
        next_day_temperature.append(r['list'][i]['main']['temp'])
        icon.append(r['list'][i]['weather'][0]['icon'])


    icon.append(r['list'][0]['weather'][0]['icon'])
    try:
        aqi= x['data']['aqi']
    except:
        aqi= 'Nie ma informacji'
    try:
        co= x['data']['iaqi']['co']['v']
    except:
        co= 'Nie ma informacji'
    try:
       no2= x['data']['iaqi']['no2']['v']
    except:
        no2= 'Nie ma informacji'
    try:
       o3= x['data']['iaqi']['o3']['v']
    except:
        o3= 'Nie ma informacji'
    try:
       pm10= x['data']['iaqi']['pm10']['v']
    except:
        pm10= 'Nie ma informacji'
    try:
       pm25=  x['data']['iaqi']['pm25']['v']
    except:
        pm25= 'Nie ma informacji'
    try:
       so2=  x['data']['iaqi']['so2']['v']
    except:
        so2= 'Nie ma informacji'
    try:
        temp = r['list'][0]['main']['temp']

    except:
        try:
            temp = x['data']['iaqi']['t']['v']
        except:

            temp= 'Nie ma informacji'
    try:
        local=x['data']['city']['name']
        print(x)
    except:
        local=''
    try:
        lat=r['city']['coord']['lat']
        lon=r['city']['coord']['lon']

    except:
        lat = x['data']['city']['geo'][0]
        lon = x['data']['city']['geo'][1]

    try:
        link=x['data']['attributions'][0]['url']
    except:
        link='none'
    try:
        name=x['data']['attributions'][1]['name']
    except:
        name = 'none'
    print()
    try:
        if  str(x['data']['city']['geo'][0]).split('.')[0]!=str(r['city']['coord']['lat']).split('.')[0]:
            name='none'
            link='none'
            local='none'
    except:
        name = 'none'
        link = 'none'
        local = 'none'
    weather = {
        'city' : str.title(request.POST['search']),
        'local': local,
        'aqi':aqi,
        'time': str(datetime.now().date()),
        'aqi_co':co ,
        'aqi_no2':no2 ,
        'aqi_o3': o3,
        'aqi_pm10':pm10 ,
        'aqi_pm25':pm25,
        'aqi_so2': so2,
        'aqi_t': temp,
        'feels_like': fell_like,
        'icon': icon[5],
        'icon1': icon[0],
        'icon2': icon[1],
        'icon3': icon[2],
        'icon4': icon[3],
        'icon5': icon[4],
        'next_day1': next_day[0],
        'next_day2': next_day[1],
        'next_day3': next_day[2],
        'next_day4': next_day[3],
        'next_day5': next_day[4],
        'next_day_temperature1': next_day_temperature[0],
        'next_day_temperature2': next_day_temperature[1],
        'next_day_temperature3': next_day_temperature[2],
        'next_day_temperature4': next_day_temperature[3],
        'next_day_temperature5': next_day_temperature[4],
        'form':form,
        'description': r['list'][0]['weather'][0]['description'],
        'log':lon,
        'lan':lat,
        'name':name,
        'link':link,


    }
    context={'weather': weather}

    return render(request, 'weather/index.html', context)



def map(request):
    mapbox_access_token = 'pk.eyJ1IjoibmlraXRhMTIzMzIxIiwiYSI6ImNsYmU5MDFjczAxcHEzb25hZ2RmZDQyYW0ifQ.uWSDZEwjQhWDOJIvmxYEHA'
    return render(request, 'weather/map.html',{'mapbox_access_token': mapbox_access_token})


