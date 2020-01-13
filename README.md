# Scale Simulator Parser

A Python-based parser to an API for my [Scale Simulator](https://github.com/DDuunk/scale-simulator.git) written for Raspberry Pi.

# Dependencies

* [Python3](https://www.python.org/download/releases/3.0/)
* Pip3
* [PySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html)
* [SocketIo](https://python-socketio.readthedocs.io/en/latest/server.html)

# Usage

To get started clone this repo or download zip and extract on your local machine. To clone using git:

```shell
$ git clone https://github.com/DDuunk/scale-simulator-parser.git
```

## Specify serial port

This project includes a `./src/serial_ports.py` file, this file is used for getting the correct serial port number.
To execute this file, run the following command

```shell
python3 src/serial_ports.py
```

The result should be content ```['/dev/ttyACM0', '/dev/ttyAMA0']```.
In this case the correct port is `/dev/ttyACM0`.
If you are not sure which port is the correct one execute the file twice, once with the cable connected and once disconnected. 
*Note: port /dev/ttyAMA0 can be ignored as it is used by UART*

Open the `./src/parser.py` file in your editor and set the serial port to your acquired port.

## Specify API details

*Note: make sure your api has SocketIO integrated for the application to work (see: https://socket.io/)*

Open the `./src/parser.py` file in your editor and set the variable `api_endpoint` to the address of your API.

## Socket events

Socket.IO works with named events, by specifying a specific event you're able to read and write messages.

For example: 

```python
import socketio

sio = socketio.Client() # Define a socket client

@sio.on('readEvent') # If the API emit's a message on the readEvent event
def on_message(data): # the on_message() function gets called
  # Handle your data
  # and maybe send data back to the API by:
  sio.emit('writeEvent', data)

sio.connect(api_endpoint) # Connect with API via a socket
sio.wait() # Wait for messages from the api
```

On the API side, you're now able to read the message via the `writeEvent` event.

# Application usage

To use the application simply run parser.py by using the following command: 

```shell
python3 src/parser.py
```