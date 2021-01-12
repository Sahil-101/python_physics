import math

g = 9.8
h = 4
t1 = math.sqrt(2*h/g)
print(t1)
e = 0.9
v = math.sqrt(2*g*h)

def get_bounce_num(t):
    temp1 = 0
    temp = t1
    temp1 = temp
    count=0

    while(temp<t):
        temp1 =temp
        temp =  temp + (pow(e , count+1))*t1*2
        count += 1
    #print(count , temp1)

    return [count, temp1]

def get_xy(t):
    g = 9.8
    h = 4
    x = 1*t
    t1 = math.sqrt(2*h/g)
    y=0
    bounce = []
    time_interval = 0
    u = 0

    if(t<t1):
        y = 1/2*g*t*t
        return (x, y)

    else:
        bounce = get_bounce_num(t)
        time_interval = t - bounce[1]
        u = pow(e , bounce[0])*v
        y = u*time_interval - (1/2)*g*time_interval*time_interval
        #print("\n" , bounce)
        return (x, y)



print(get_xy(1))
print(get_xy(2))
print(get_xy(3))
print(get_xy(4))
print(get_xy(5))
print(get_xy(6))
print(get_xy(6.3))
print(get_xy(6.4))
