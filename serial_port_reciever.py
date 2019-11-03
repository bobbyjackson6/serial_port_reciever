import serial

ser=serial.Serial()
ser.baudrate=9600
port_input = input('Введите порт приема(я ставил 2): ')
ser.port='COM'+port_input
ser.open()
while True:
    getting_x = ser.readline(3)
    getting_y = ser.readline(3)
    getting_rgb = ser.readline(21)
    print(getting_x)
    print(getting_y)
    print(getting_rgb)