from serial.tools import list_ports
from serial import Serial

def get_arduino():
    arduinos = []
    for port in list_ports.comports():
        if port.manufacturer and "arduino" in port.manufacturer.lower():
            arduinos.append(port.device)
    return arduinos

class Link:
    def __init__(self, port="/dev/ttyACM0", baudrate=115200):
        self.ser = Serial(port, baudrate, timeout=0.5)
        self.ser.flush()
        self.data = ""
        self.new_data = False
        self.start_marker = "<"
        self.end_marker = ">"
        self.incoming_in_process = False
        self.incoming_data = ""

    def read(self):
        try:
            while self.ser.inWaiting() > 0:
                data = self.ser.read().decode()
                if(data == self.start_marker):
                    self.incoming_in_process = True
                    #self.new_data = False
                    self.incoming_data = ""
                elif(data == self.end_marker):
                    self.incoming_in_process = False
                    self.data = self.incoming_data
                    self.incoming_data = ""
                    self.new_data = True
                elif (self.incoming_in_process == True):
                    self.incoming_data += data
        except Exception as e:
            print(e)

    def get_name(self):
        self.ser.write(b"#")
    
    def write(self, msg):
        self.ser.write(b""+self.start_marker.encode())
        self.ser.write(b""+msg.encode())
        self.ser.write(b""+self.end_marker.encode())
    
    def get_data(self):
        if self.new_data:
            self.new_data = False
            return self.data
        return ""