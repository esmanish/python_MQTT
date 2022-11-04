


import paho
import paho.mqtt.client as mqtt_client
import time

storage = []

def on_message(client,userdata,message):
	topic = str(message.topic)
	value = str(message.payload.decode("utf-8"))
	print (topic,value)
	storage.append((topic,value))





def connect():
	broker = "10.100.82.134"
	port = 1885
	client = mqtt_client.Client("Client2")
	client.connect(broker,port)
	client.loop_start()
	client.subscribe("A")
	client.subscribe("B")
	client.subscribe("C")
	client.on_message = on_message
	time.sleep(30)
	client.loop_stop()
	file  = open("LOG_FILE", "w")
	for i in storage:
		file.write(str(i)+"\n")

	file.close()







if __name__ == "__main__":
	connect()