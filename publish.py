import paho
import paho.mqtt.client as mqtt_client
import random
import time

def generate():
	topic = ["A","B","C"]
	T = topic[random.randint(0,2)]
	V = random.randint(0,100)
	return T,V

def connect():
	broker = "10.100.82.134"
	port = 1885
	client = mqtt_client.Client("Client1")
	client.connect(broker,port)
	while True:
		topic,value = generate()
		status = client.publish(topic,value)
		print("Topic:"+str(topic)+"\tValue:"+str(value))
		time.sleep(1)


if __name__ == "__main__":
	connect()