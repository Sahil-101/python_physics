import matplotlib.pyplot as plt 
import math
from matplotlib.animation import FuncAnimation

#Standard Variables and inital values
g = 9.8
h = 4
#t1 = time for the first hit to ground
t1 = math.sqrt(2*h/g)

#coefficient of restitution
e = 0.6

# speed at the touchdown to ground for the first time
v = math.sqrt(2*g*h)

#X and Y coordinates list for the trajectory
X=[0]
Y=[4]

#Static function to get the no. of times the ball has been hit before the given time
def get_bounce_num(t):
    temp1 = 0
    temp = t1
    temp1 = temp
    count=0

    while(temp<t):
        temp1 =temp
        temp =  temp + (pow(e , count+1))*t1*2
        count += 1

    return [count, temp1]

#function to get x , y coordinates at a given instant of time
def get_xy(t):
    x = 1*t
    y=0
    bounce = []
    time_interval = 0
    u = 0

    if(t<t1):
        y = 4 - 1/2*g*t*t
        return (x, y)

    else:
        bounce = get_bounce_num(t)
        time_interval = t - bounce[1]
        u = pow(e , bounce[0])*v
        y = u*time_interval - (1/2)*g*time_interval*time_interval
        return (x, y)

#time variable
i=0

#getting coordinates and adding it to LIST
while(i<3.5):
    coordinates = get_xy(i)
    X.append(coordinates[0])
    Y.append(coordinates[1])
    i+=0.01

#plotting the graph :)
fig, ax = plt.subplots()

ax.set_title ("Trajectory of ball, with e = " + str(e))
ax.set_ylabel('Height of the ball') 
ax.set_xlabel('Horizontal distance covered')
ax.plot(X, Y, "r")
plt.xlim(0)
plt.ylim(0)


plt.show()
