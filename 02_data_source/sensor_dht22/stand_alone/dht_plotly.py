import plotly.plotly as py
import Adafruit_DHT as dht # Adafriut_DHT requireds sudo
import json
import time
import datetime


print 'Temperature & Humidity sensor node'

# streaming of temparure data to plotly every 10sec for 24h plot (= 8640 data points)

divID = 'dht22_001'

# load authentification and streaming details 
with open('../configPlotly.json') as config_file:
        plotly_user_config = json.load(config_file)


while True:
        py.sign_in(plotly_user_config['plotly_username'],plotly_user_config['plotly_api_key'])

        #inits chart at plot.ly - to feed addtional data into chart, do not re-init
        #url = py.plot([
        #    {
        #        'x': [], 'y': [], 'type': 'scatter',
        #        'stream': {
        #            'token': plotly_user_config['plotly_streaming_tokens'],
        #            'maxpoints': plotly_user_config['plotly_max_data_points']
        #        }
        #    }], filename='Raspberry Pi Streaming Example Values')
        #print "Streaming url: ", url
        
        print 'streaming started.. '  

        stream = py.Stream(plotly_user_config['plotly_streaming_tokens'])
        stream.open()
        try:
                while True:
                        h, t = dht. read_retry(dht.DHT22, 4)
                        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                        # print json.dumps({'temperature' : t , 'humidity' : h , 'timestamp' : ts },sort_keys=False, indent=4, separators=(',', ': '))
                        stream.write({'x': ts, 'y': t })        
                        # delay between stream posts        
                        print '.'  
                        time.sleep(10)
        except ValueError:
                ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                print "streaming disconnected at ", ts
        time.sleep(20)
