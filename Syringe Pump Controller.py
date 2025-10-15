import serial
import time 

port = serial.Serial('COM3', 19200, parity=serial.PARITY_NONE, bytesize=8, stopbits=1, timeout=None, xonxoff=0, rtscts=0) #Open serial port using settings required by pump on COM3

def send_cmd(cmd):
    port.write((cmd + '\r\n').encode())
    time.sleep(0.1)

Pump_Program = """
*ADR CONT
*DIA 29.20
*VOL ML

*PHN 1
*FUN RAT 
*RAT 005.0 MM 
*VOL 10.00 

*PHN 2
*FUN RAT
*RAT 07.00 MM 
*VOL 0.000

*PHN 3 
*FUN RAT
*RAT 005.0 MM 
*VOL 0.100

*PHN 4
*FUN RAT
*RAT 0011 MH
*VOL 0.000 

"""

send_cmd("*STP")

time.sleep(0.1)

send_cmd("*RESET")

time.sleep(0.1)

for line in Pump_Program.split('\n'):
    line = line.strip()
    if line:
        send_cmd(line)

time.sleep(0.1)

send_cmd("RESET")

time.sleep(0.1)

send_cmd("*RUN")

port.close()