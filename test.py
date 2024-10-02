import serial

port = "COM3"  # UART5 portu
baud_rate = 9600

# Seri portu başlat
ser = serial.Serial(port, baud_rate)

while True:
    RTS_status = ser.getCTS()
    if RTS_status:
        print("ON")
    else:
        print("OFF")