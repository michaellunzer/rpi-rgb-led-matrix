import  pywapi
import string

weather_com_result = pywapi.get_weather_from_weather_com('97210', 'imperial')
yahoo_result = pywapi.get_weather_from_yahoo('97210', 'imperial')
noaa_result = pywapi.get_weather_from_noaa('KPDX')

print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "F now in Portland.\n\n"

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "F now in Portland.\n\n"

print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_f'] + "F now in Portland.\n"
