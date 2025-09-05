import serial
import time 

port = serial.Serrial('COM1', 19200, parity=serial.PARITY_NONE, bytesize=8, stopbits=1, timeout=None, xonoff=0, rtscts=0) #Need to look into xonxoff, possibly related to firmware

def send_cmd(cmd):
    port.write((cmd + '\r\n').encode())
    time.sleep(0.1)

Pump_Program = """
DIA 36.50

PHN 1
FUN RAT
RAT 100 MH
VOL 45
DIR INF

PHN 2
FUN RAT
RAT 500 MH 
VOL 0
DIR WDR 

PHN 3
FUN RAT
RAT 200 MH 
VOL 0.1
DIR INF

PHN 4
FUN RAT
RAT 11 MH 

DIR STK
"""
for line in Pump_Program.split('\n'):
    line = line.strip()
    if line:
        send_cmd(line)

send_cmd("RUN")

port.close()