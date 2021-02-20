import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import time

count = 1
 
style.use("dark_background")

fig = plt.figure()
fig.suptitle('Black Betty Data')
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)


def animate(i):
    graph_data = open("C:/Users/Christine/Desktop/dataGps/data.txt","r").read()
    lines = graph_data.split('\n')
    
    xs = []
    ys = []
    zs = []
    accel_x = []
    accel_y = []
    accel_z = []
    oilPress = []
    engTemp = []
    time = []
    
    for line in lines:
        if len(line) > 1:
            utc, lat, lon, alt, spd, acx, acy, acz, ai1 = line.split(',')
            if float(lat) < 100000 or float(lon) < 100000:
                continue
            xs.append(float(lat))
            ys.append(float(lon))
            zs.append(float(spd)*0.621)
            accel_x.append(float(acx))
            accel_y.append(float(acy))
            accel_z.append(float(acz))
            oilPress.append(((float(ai1)/100)*21.875)-15.188)
            #engTemp.append(((float(ai2)/100)*21.875)-15.188)
            time.append(utc)
    
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    
    sf1_lat = 36.5692830*100000
    sf1_lon = -79.2066920*-100000
    sf2_lat = 36.5682980*100000
    sf2_lon = -79.2065510*-100000

    #xs = xs[-200:]
    #ys = ys[-200:]
    #ax1.scatter(xs,ys,color='blue')
    #xs = xs[-1]
    #ys = ys[-1]
    #ax1.scatter(xs,ys,color='red')

    # ADD WITH ENG TEMP SENSOR
    #xsTemp = xs[-200:]
    #ysTemp = ys[-200:]
    #plt1 = ax1.scatter(xsTemp,ysTemp,c = engTemp[-200:],vmin=160,vmax=230,cmap='jet_r')
    #if i == 1:
    #    cm = plt.colorbar(1)

    ax2.bar(1,zs[-1],color = 'b')
    ax2.bar(2,oilPress[-1],color = 'b')
    ax2.set_xticks([1,2])
    ax2.set_xticklabels(['Speed (MPH)','Oil Press (PSI)'])
    ax2.set_ylim([0,160])
    ax2.text(1,zs[-1]+7.5,str(int(zs[-1])),color='white',fontweight='bold')
    ax2.text(2,oilPress[-1]+7.5,str(int(oilPress[-1])),color='white',fontweight='bold')

    accel_x = accel_x[-1]/(9.81*100)
    accel_y = accel_y[-1]/(9.81*100)
    accel_z = accel_z[-1]/(9.81*100)
    ax3.scatter(accel_x,accel_y,250,color='blue')
    ax3.set_xlim([-2,2])
    ax3.set_ylim([-2,2])
    ax3.set_xlabel('Longitinal Accel [g]')
    ax3.set_ylabel('Lateral Accel [g]')

    xsTemp = xs[-200:]
    ysTemp = ys[-200:]
    plt4 = ax4.scatter(xsTemp,ysTemp,c = oilPress[-200:],vmin=0,vmax=60,cmap='jet_r')
    if i == 1:
        cm = plt.colorbar(plt4)
        
    ax1.axis('equal')
    ax1.set_title('Location')
    ax2.set_title('Gauges')
    ax4.set_title('Oil Pressure [PSI]')

    #ax1.grid()
    ax2.grid(axis='y')
    ax3.grid()
    #ax4.grid()

    ax1.set_xticks([])
    ax1.set_yticks([])

    ax4.set_xticks([])
    ax4.set_yticks([])
    
    ax1.axis('equal')
    ax1.set_xlabel('latitude*100000')
    ax1.set_ylabel('longitude*100000')
    
    ax4.axis('equal')
    ax4.set_xlabel('latitude*100000')
    ax4.set_ylabel('longitude*100000')

    ## Debug Print
    print('DAQ Time: ' + time[-1])
    print('Current Time: ' + str(datetime.utcnow()))
    print('Data File Length: ' + str(len(lines)))


ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()



