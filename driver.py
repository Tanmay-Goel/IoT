import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
prevval=""
user=''
mydict={}
from BackEnd import *
user_tags=['5500E4029B28','5500E477DB1D']
item_tags=['5500C7E71C69','5500CF40FD27','5500E7EF5409']

def Entry():
    etag=rfid()
    if etag in user_tags:
        servo()

def Exit():
    val=rfid()
    if val in user_tags:
        a=billcalc(val)
        if(a==True):
            servo()
            del mydict[val]
        else:
            print("insufficient balance")

def billcalc(val):
    if val not in mydict:
        return True
    elif val in d:
        cost=0
        for k,v in mydict.items():
            for k1,v1 in v.items():
		cursor.execute("SELECT ITEM_COST FROM ITEM_LIST WHERE ITEM_ID=?",(k1))
                r=cursor.fetchone()
                cost+=r*v1
        cursor.execute("SELECT BALANCE FROM CUSTOMER WHERE CUS_ID=?",(val))
        rr=cursor.fetchone()
        if(cost<=rr):
            return True
    else:
        return False

def rfid ():
   ser = serial.Serial ("/dev/ttyS0")                           #Open named port 
   ser.baudrate = 9600                                            #Set baud rate to 9600
   data = ser.read(15)                                            #Read 12 characters from serial port to data
   ser.close ()                                                   #Close port
   return data   

def servo():
    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    GPIO.cleanup()

def itemtagcheck(tag):
    if tag in item_tags:
        if prevval==''
            print("Activate Trolley")
        else:
            for i,j in mydict.items():
                if tag in j.keys():
                    for x,y in j:
                        if x==tag:
                            y+=1
                else:
                    j[tag]=1
                            
    prevval=tag   


def usertagcheck (val):
   if val in user_tag:
      del mydict[val][preval]
   else:
      mydict[val]={}
      prevval=val


while(True):
    Entry()
    tag=input("Enter tag-id")
    if tag in user_tags:
        usertagcheck(tag)
    elif tag in item_tags:
        itemtagcheck(tag)
    Exit()    
