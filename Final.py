import time
import serial
import sys
# To make .exe : Open cmd in location; pyinstaller --onefile -w Ssms.py
# add message as string ex: python Ssms.py "High Pressure" +916281439495
# Ssms.exe "High Pressure" "+916281439495" "+919848299811" "+919676760679"
message = sys.argv[1]
recipients = sys.argv[2:len(sys.argv)]

phone = serial.Serial("com2",  115200, timeout=5)


def send_sms(number):
    phone.write(b'ATZ\r')
    time.sleep(0.1)
    # to read response: print(phone.readline(15)) 15 or number depends on response
    phone.write(b'AT+CMGF=1\r')
    time.sleep(0.1)  # Use sleep  or  if b'OK in phone.readline(15)
    phone.write(b'AT+CMGS="' + number.encode() + b'"\r')
    time.sleep(0.3)
    phone.write(message.encode() + b"\r")
    time.sleep(0.3)
    phone.write(bytes([26]))  # equivalent to Ctrl + Z in Hyperterminal
    time.sleep(0.5)


for rec in recipients:
    send_sms(rec)
    time.sleep(1.8)

phone.close()


'''Hyperterminal commands:
AT
AT+CMGF=1
AT+CMGS="+916281439495"
>"TEST MESSAGE"
>Ctrl + Z
'''
