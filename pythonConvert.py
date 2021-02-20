import serial
import numpy as np
from functools import reduce
from operator import concat
from datetime import datetime
from time import sleep

print("Initializing...")

init = 0
while init == 0:
    try:
        port = "COM11"
        ser = serial.Serial(port,9600)
        data = 0
        dataRaw = 0
        data = np.chararray(255)
        init = 1
    except:
        sleep(1)
        print("Intialization Error On Port: "+str(port))

print("Initialized...")
        
while 1:
    data = np.chararray(255)
    for n in range(255):
        dataRaw = (ser.read())
        try:
            data[n] = dataRaw
        except:
            print("nullDataAssign")
        if dataRaw == b'\n':
            print("Data Parsed...")
            #print(data)   
            try:
                data = data[0:63].decode('utf-8')
                print(reduce(concat,(data)))
                file = open("C:/Users/Christine/Desktop/dataGps/data.txt","a")
                file.write(str(datetime.utcnow())+','+str(reduce(concat,(data))))
                file.write("\n")
                file.close()
                print("Data Saved...")
            except:
                print("nullConcat")
            break

        




