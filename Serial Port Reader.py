import serial
import time 
import keyboard

def key_press(event):   #Break loop when Q is pressed on keyboard
    global running
    if event.name == 'q':
        running = False

def serial_listen():
    running = True
    keyboard.on_press(key_press)

    while running:
        port = serial.Serial('COM3', 19200, parity=serial.PARITY_NONE, bytesize=8, stopbits=1, timeout=None, xonxoff=0, rtscts=0) #Open serial port using settings required by pump on COM3
        x = serial.readline()
        
        print (x)
    
    port.close()
    print("Program ended by keypress.")

if __name__ == "__main__":
    serial_listen()
