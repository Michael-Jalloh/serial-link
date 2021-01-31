This is a simple library that helps in serial communication between arduino using the link arduino library and a host computer.

# Requiements
1. PySerial

# Usage

```
from serial import Serial

from link import Link

def run(port="/dev/ttyACM0"):
    l = Link(port)
    while 1:
        l.read()
        if l.new_data:
            data = l.get_data()
            print(data)

if __name__=="__main__":
    run()
```
