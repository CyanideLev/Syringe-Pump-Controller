import serial
import time 
import cv2

def serial_listen():
    
    port = serial.Serial('COM4', 19200, parity=serial.PARITY_NONE, bytesize=8, stopbits=1, timeout=None, xonxoff=0, rtscts=0)

    print ('Listening...')

    while (True):
        
        x = port.readline()
        
        print (x + '\r\n')
        
        if cv2.waitkey(1)==ord('q'):
            break
    
    port.close()
    print("Program ended by keypress.")

if __name__ == "__main__":
    serial_listen()
