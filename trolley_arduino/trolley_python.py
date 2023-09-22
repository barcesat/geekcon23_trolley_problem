import serial
import time

# Define the Arduino serial port (change this to your actual port)
arduino_port = 'COM3' #'/dev/ttyUSB0'  # Replace with your Arduino's port (e.g., 'COM3' on Windows)

# Establish a serial connection with the Arduino
ser = serial.Serial(arduino_port, 9600, timeout=1)

def send_command(command):
    ser.write(command.encode())
    ser.flush()  # Flush the serial buffer to ensure no old data is read
    response = ser.readline().decode().strip()
    return response

try:
    while True:
        user_input = input("Enter command (A, B, R, S, 1, 2): ")
        if user_input == 'A':
            response = send_command('A')
            print(response)
        elif user_input == 'B':
            response = send_command('B')
            print(response)
        elif user_input == 'R':
            response = send_command('R')
            print(response)
        elif user_input == 'S':
            response = send_command('S')
            print(response)
        elif user_input == '1':
            response = send_command('1')
            print(response)
        elif user_input == '2':
            response = send_command('2')
            print(response)
        else:
            print("Invalid command")
        

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
