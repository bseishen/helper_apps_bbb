import time
import requests
get_response = requests.get(url='http://google.com')
w1="/sys/bus/w1/devices/10-000802415f85/w1_slave"

while True:
    raw = open(w1, "r").read()
    temperature = float(raw.split("t=")[-1])/1000
    print str(temperature)
    temperature = 1.8*temperature + 32    
    print "Temperature is "+str(temperature)+" degrees"
    url = "http://192.168.1.230/emoncms/feed/update.json?id=1&apikey=ad2fea5703561987429cd8c5506072c5&time=UNIXTIME&value="+str(temperature)
    print url	
    get_response = requests.get(url)
    print get_response
   
    time.sleep(1)
