import serial
import time 

port = serial.Serial('COM3', 19200, parity=serial.PARITY_NONE, bytesize=8, stopbits=1, timeout=None, xonxoff=0, rtscts=0) #Open serial port using settings required by pump on COM3

def send_cmd(cmd):
    port.write((cmd + '\r\n').encode())
    time.sleep(0.1)

Pump_Program = """
DIA 29.20
VOL ML
TRGFT
AL 0
PF 0
BP 0

PHN 1 
FUN RAT 
RAT 100 MH 
VOL 5

PHN 2 
FUN RAT
RAT 500 MH 
VOL 0

PHN 3 
FUN RAT
RAT 200 MH 
VOL 0.1

PHN 4 
FUN RAT
RAT 11 MH
"""

for line in Pump_Program.split('\n'):
    line = line.strip()
    if line:
        send_cmd(line)

send_cmd("RUN")

port.close()