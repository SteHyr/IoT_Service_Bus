import Adafruit_DHT as dht # Adafriut_DHT requireds sudo
import json
import time
import datetime
import MySQLdb

i = 0
divID = 'dht22_001'

#constructor / connect to DB
db = MySQLdb.connect('localhost', 'monitor3', 'a', 'sensorDB')
cursor = db.cursor()

#db check
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "MySQL version: %s" % data

#the main sensor reading and DB upload loop
try:
        while True:	
                h, t = dht. read_retry(dht.DHT22, 4)
                ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		querry = "INSERT INTO sensorData(i, divID, timeStamp, temp, humi) VALUES ('%d', '%s', '%s', '%f', '%f')" % (i, divID, ts, t, h)
	
		cursor.execute(querry)
                #print json.dumps({'index': i , 'temperature' : t , 'humidity' : h , 'timestamp' : ts },sort_keys=False, indent=4, separators=(',', ': '))
        	db.commit()
                i = i + 1

# something went wrong
except MySQLdb.Error, e:
	print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
	db.rollback()

#deconstructor after error
finally:
	if db:
		db.close()
		print "DB closed after error"
