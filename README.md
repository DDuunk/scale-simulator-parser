# Scale Simulator Parser

A Python-based parser for my [Scale Simulator](https://github.com/DDuunk/scale-simulator.git) written for Raspberry Pi.

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

To search for available serial ports on Raspberry Pi use the following command

```shell
ls /dev/tty*
```

The result should be content ```/dev/ttyACM0``` and you are good to go.

Open the `./src/parser.py` file in your editor and set the serial port to your acquired port.

# Application usage

To use the application simply run parser.py by using the following command: 

```shell
python3 src/parser.py
```