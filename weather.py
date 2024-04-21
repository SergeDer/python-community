import httpx

class Weather:    
    URL='http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=no'
    weather = ''
    def __init__(self, API_KEY, town) -> None:
        self.url = Weather.URL.format(API_KEY, town)        
    def get_weather(self):
        try:             
            responce = httpx.get(self.url)
            r = responce.json()
            if responce.status_code == 200:                
                self.weather = (
                    f"{r['location']['name']}_{r['current']['last_updated']}_"
                    f"{r['current']['temp_c']}_C_{r['current']['feelslike_c']}_feelslike_C_{r['current']['condition']['text']}_"
                    f"{r['current']['humidity']}_%Hum_{r['current']['wind_kph']}_Wind_kph")
            else:
                print(r)            
        except:
            print('ConnectionError')
        

v = Weather('da30ffdfe36249148401258492415041', 'London')
v.get_weather()
print(v.weather)



