import requests
import time




time_clokc = '15:00:00'
next_day=[]
next_day_temperature=[]
icon=[]

den=0


def index():

        cityname = 'lida'
        PARAMS = {'q': cityname, 'units': 'metric'}


        response = requests.get(
                url='https://api.waqi.info/feed/' + cityname + '/?token=840733e07b0dd7eaafa5453a8dce5e1ff715e43e')
        URL = 'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=13,4&lon=12,3&appid=3b02ead1885113bcf888c7e1fb750c2e'
        coord='http://api.openweathermap.org/geo/1.0/direct?q='+cityname+'&limit=5&appid=3b02ead1885113bcf888c7e1fb750c2e'

        x2 = requests.get(url=coord) #params=PARAMS)

        r = x2.json()
        x = response.json()
        for i in r:
                print(r[0]['lat'])
                print(r[0]['lon'])

        time_clokc = '15:00:00'
        next_day = []
        next_day_temperature = []
        den = 0
        fell_like = []
        icon = []
        print(r[0]['name'])
      #  print (x['data']['time']['s'])
        for k in range(5):
                i = 0
                if x['data']['time']['s'][:-8][8:10][0] == '0':
                        den = int(x['data']['time']['s'][:-8][8:10][1])
                else:
                        den = int(x['data']['time']['s'][:-8][8:10])
                year = int(x['data']['time']['s'][:-8][0:4])
                month = int(x['data']['time']['s'][:-8][5:7])
                den += 1 + k
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
                                        print('GG')

                try:
                        while r['list'][i]['dt_txt'] != str(
                                str(year) + '-' + str(month) + '-' + '0' + str(den) + ' ' + time_clokc):
                                print(  str(year) + '-' + str(month) + '-' + '0' + str(den) + ' ' + time_clokc)
                                i += 1
                except:
                        while r['list'][i]['dt_txt'] != str(str(year) + '-' + str(month) + '-' + str(den) + ' ' + time_clokc):
                                i += 1
                next_day.append(r['list'][i]['dt_txt'][:-8])
                next_day_temperature.append(r['list'][i]['main']['temp'])
                icon.append(r['list'][i]['weather'][0]['icon'])

index()

