import serial
import time
import platform

class ArduinoController:
    def __init__(self, port=None):
        self.port_opened_successfully = False
        if port is None:
            # Detect the operating system and set the Arduino serial port accordingly
            if platform.system() == "Windows":
                self.arduino_port = 'COM3'  # Replace with the correct COM port for Windows
            elif platform.system() == "Linux":
                self.arduino_port = '/dev/ttyACM0'  # Replace with the correct serial port for Linux
            else:
                raise Exception("Unsupported operating system")
        else:
            self.arduino_port = port
        
        try:
            # Attempt to establish a serial connection with the Arduino
            self.ser = serial.Serial(self.arduino_port, 9600, timeout=1)
            time.sleep(2)  # Allow some time for the Arduino to initialize
            self.port_opened_successfully = True
        except Exception as e:
            print(f"Failed to open port {self.arduino_port}: {e}")

    def send_command(self, command):
        if not self.port_opened_successfully:
            return "Port not open successfully"
        self.ser.write(command.encode())
        response = self.ser.readline().decode().strip()
        return response

    def toggle_relay_1(self):
        return self.send_command('A')

    def toggle_relay_2(self):
        return self.send_command('B')

    def restart_train(self):
        return self.send_command('R')

    def stop_train(self):
        return self.send_command('S')

    def choose_track_1(self):
        return self.send_command('1')

    def choose_track_2(self):
        return self.send_command('2')

    def close_connection(self):
        self.ser.close()

# Example usage:
if __name__ == "__main__":
    # You can specify the COM port as an argument when creating an instance of ArduinoController
    # com_port = input("Enter the COM port (e.g., COM3 or /dev/ttyUSB0): ")
    arduino = ArduinoController()#port=com_port)
    if arduino.port_opened_successfully:
        try:
            while True:
                user_input = input("Enter command (A, B, R, S, 1, 2): ")
                if user_input == 'A':
                    response = arduino.toggle_relay_1()
                elif user_input == 'B':
                    response = arduino.toggle_relay_2()
                elif user_input == 'R':
                    response = arduino.restart_train()
                elif user_input == 'S':
                    response = arduino.stop_train()
                elif user_input == '1':
                    response = arduino.choose_track_1()
                elif user_input == '2':
                    response = arduino.choose_track_2()
                else:
                    response = "Invalid command"

                print("Arduino Response:", response)

        except KeyboardInterrupt:
            print("Exiting...")
            arduino.close_connection()
