import time

old_data = open("C:/Users/Christine/Desktop/dataGps/data_DIS20.txt","r").read()
lines = old_data.split('\n')
count = 1
for line in lines:
    count = count + 1
    if count > 8800:
        print(line)
        file = open("C:/Users/Christine/Desktop/dataGps/data.txt","a")
        file.write(line)
        file.write("\n")
        file.close()
        time.sleep(0.75)
    
    


