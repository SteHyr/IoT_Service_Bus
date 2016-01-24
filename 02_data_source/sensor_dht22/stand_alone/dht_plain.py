import Adafruit_DHT as dht # Adafriut_DHT requireds sudo
import json
import time
import datetime

while True:
        h, t = dht. read_retry(dht.DHT22, 4)
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print json.dumps({'temperature' : t , 'humidity' : h , 'timestamp' : ts },sort_keys=False, indent=4, separators=(',', ': '))
