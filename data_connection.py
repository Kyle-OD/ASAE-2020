import time
import serial


def meters_to_feet(meters):
    feet = 3.28*meters
    return feet


data_out = "from_the_air.txt"
data_in = "from_ground_command.txt"

serial = serial.Serial(port="COM8", baudrate=9600)
time.sleep(1)

while True:
    data_in_file = open(data_in)
    write = data_in_file.read()
    serial.write(str.encode(write))
    data_in_file.close()
    while serial.inWaiting() < 0:
        time.sleep(0.1)
    read = serial.readline()
    read = bytes.decode(read)
    print(read)
    data_out_file = open(data_out, "w")
    data_out_file.write(read)
    data_out_file.close()
    time.sleep(0.1)


