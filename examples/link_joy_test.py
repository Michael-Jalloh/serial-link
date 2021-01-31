from serial_link import Link

def run(port="/dev/ttyUSB0"):
    l = Link(port)
    while 1:
        l.read()
        if l.new_data:
            data = l.get_data().split(";")
            print(f"SW: {data[0]}")
            print(f"X: {data[1]}")
            print(f"Y: {data[2]}")
            print("==========================*==========================")

if __name__ == "__main__":
    port =input("Please Enter port: ")
    run(port)