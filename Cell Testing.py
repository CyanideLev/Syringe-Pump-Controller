import serial
import time
import keyboard
import multiprocessing as mp
import piplates.THERMOplate as THERMO

def key_press(event):   #Break loop when Q is pressed on keyboard
    global running
    if event.name == 'q':
        running = False

def temp_read(conn):
    print('Thermocouple: Running', flush=True)
    while(True):

        t2=THERMO.getTEMP(0,2)
        time.sleep(.05)
        conn.send(t2)
        
        link_state = 1

        if link_state is None:
            break

def pump_ctrl():

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

def mfc_ctrl(): #need to check specifics for Alicat Scientific MC-20SmLPM-D
    port = serial.Serial('COM2', 19200, parity=serial.PARITY_NONE, bytesize=8, stopbits=1, timeout=None, xonxoff=0, rtscts=0)

    #Code 

    p1.terminate()

if __name__ == "__main__":
    
    conn1, conn2 = mp.Pipe()
    p1 = mp.Process(target=temp_read, args=(conn1,))
    #p2 = mp.Process(target=mfc_ctrl, args=(conn2,))
    p1.start()
    time.sleep(5)
    #p2.start()
    p1.join()
    #p2.join()
