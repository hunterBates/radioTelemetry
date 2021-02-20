import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime

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
    time = []
    
    for line in lines:
        if len(line) > 1:
            utc, lat, lon, alt, spd, acx, acy, acz, ai1 = line.split(',')
            xs.append(float(lat))
            ys.append(float(lon))
            zs.append(float(spd))
            accel_x.append(float(acx))
            accel_y.append(float(acy))
            accel_z.append(float(acz))
            oilPress.append(float(ai1))
            time.append(utc)
    
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    
    xs = xs[-200:]
    ys = ys[-200:]
    ax1.scatter(xs,ys,color='blue')
    xs = xs[-1]
    ys = ys[-1]
    ax1.scatter(xs,ys,color='red')

    zs = zs[-1]
    ax2.bar(['Speed'],zs, color = 'b')
    ax2.set_ylabel('Miles Per Hour')
    ax2.set_ylim([0,135])

    accel_x = accel_x[-1]/(9.81*100)
    accel_y = accel_y[-1]/(9.81*100)
    accel_z = accel_z[-1]/(9.81*100)
    ax3.scatter(accel_x,accel_y,250,color='blue')
    ax3.set_xlim([-2,2])
    ax3.set_ylim([-2,2])
    ax3.set_xlabel('Longitinal Accel [g]')
    ax3.set_ylabel('Lateral Accel [g]')

    oilPress = ((oilPress[-1]/100)*21.875)-15.188
    ax4.bar(['Oil Pressure'],oilPress, color = 'b')
    ax4.set_ylabel('Pounds Per Square Inch')
    ax4.set_ylim([0,70])
    
    ax1.axis('equal')
    ax1.set_xlabel('latitude*100000')
    ax1.set_ylabel('longitude*100000')

    ax1.grid()
    ax2.grid()
    ax3.grid()
    ax4.grid()

    ## Debug Print
    print('DAQ Time: ' + time[-1])
    print('Current Time: ' + str(datetime.utcnow()))
    print('Data File Length: ' + str(len(lines)))

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()



