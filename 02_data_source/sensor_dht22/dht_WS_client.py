import websocket
import thread

import Adafruit_DHT as dht # Adafriut_DHT requireds sudo
import json
import time
import datetime

with open('/home/pi/configDevice.json') as config_file:
    device_infos = json.load(config_file)
device_id = device_infos['device_ID']


with open('/home/pi/configBrocker.json') as config_file:
    brocker_infos = json.load(config_file)
brocker_IP = brocker_infos['brocker_IP']
brocker_port = brocker_infos['brocker_port']


def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    def run(*args):
        for i in range(10):
            h, t = dht. read_retry(dht.DHT22, 4)
            ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            msg = json.dumps({'deviceID': device_id, 'temperature' : t , 'humidity' : h , 'timestamp' : ts },sort_keys=False, indent=4, separators=(',', ': '))
            ws.send(msg)
            time.sleep(10)
        ws.close()
        print "thread terminating..."
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    brocker_location = "ws://" + brocker_IP + ":" + brocker_port + "/"
    print brocker_location
    
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(brocker_location,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
