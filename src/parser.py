import serial
import time
import socketio

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
api_endpoint = 'INSERT API ADDRESS HERE'

sio = socketio.Client()

# Some basic events that might be usefull
@sio.event
def connect():
  print("Socket connected")

@sio.event
def connect_error():
  print("Socket connection failed")

@sio.event
def disconnect():
  print("Socket disconnected")

@sio.on('scale') # API emit's a message via the scale event
def on_message(data): # so we know we have to send a scale value back.
  ser.write(str.encode('S')) # The scale value is acquired by sending a 'S' to our Arduino application.
  incomingData = ser.readline().decode("utf-8") # The Arduion then sends back a random value
  incomingData = incomingData.replace("\r\n", "") # Modify the incomingData string a bit
  sio.emit('weight', incomingData) # We send the scale data back to the API using the weight event

sio.connect(api_endpoint) # Connect the socket
sio.wait() # Wait for incomming message / events