#IoT DHT sensor node

Simple python applications to read raspberry Pi GPIO data from a dht22 (temperatur & humidity sensor) 

##Realized implementations 
- The wiring of the GHT22 sensor follows this [tutorial](www.youtube.com%2Fwatch%3Fv%3DIHTnU1T8ETk) on YouTube
- To read the DHT22 sensor, the [DHT library](https://github.com/adafruit/Adafruit_Python_DHT) by Adafruit is required. The library requires sudp for excection. 


###Display values
plain output of values and timestamp as JSON dump

###Local MySQL storing
- table sensorData
 - i BIGINT
 - divID CHAR(30)
 - timeStamp CHAR(30)
 - temp DOUBLE
 - humi DOUBLE 

###[Plot.ly](https://plot.ly) upload
--> local init-file required: ../configPlotly.json  
> {  
> "plotly_streaming_tokens":"..",  
> "plotly_api_key": "..",  
> "plotly_username": "..",  
> "plotly_max_data_points" : ..  
> }  

###WebSocket upload
--> local init-file required: ../configDevice.json  
> {  
> "device_ID": ".."  
> }  
WebSocket Server displays received JSON message


