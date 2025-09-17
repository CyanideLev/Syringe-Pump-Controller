import serial
import time 
import os, sys

port = serial.Serial('COM3', 19200, parity=serial.PARITY_NONE, bytesize=8, stopbits=1, timeout=None, xonxoff=0, rtscts=0) #Open serial port using settings required by pump on COM3

def read_cmd(cmd):
    port.read()