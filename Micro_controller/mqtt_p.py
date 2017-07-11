# Setup Wifi module or GPRS module.
# Set Camera
# Take pics
# Convert to byte array
# Publish on the server in form of byte array

# That code will be in c




# Just an example of image sending in python
import paho.mqtt.client as mqtt

def on_publish(mosq, userdata, mid):
    mosq.disconnect()

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.on_publish = on_publish

f=open("lol.jpg", "rb") 
fileContent = f.read()
byteArr = bytearray(fileContent)
client.publish("image",byteArr,0)

client.loop_forever()
