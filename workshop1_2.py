%pylab inline
# Perfect sensor
def sense(x):
    return x
def simulate(Δt, x, u):
    x += Δt * u
    return x
def ud(t):
    xd = (sin(5*t)+2)*cos(t)
    yd = (sin(5*t)+2)*sin(t)
    return array([xd,yd])
def control(t, y):
    ### WRITE YOUR CONTROL POLICY HERE:
    ux = 5*cos(5*t)*cos(t)-sin(5*t)*sin(t)-2*sin(t)
    uy = 5*cos(5*t)*sin(t)+sin(5*t)*cos(t)+2*cos(t)
    return array([ux, uy])
def PIcontrol(t,y):
    ut = k1*(ud(t)- y)
    return ut
tf = 7.
Δt = 0.01    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval
def wind(y):
    y[1] = y[1] + 0.3
    return y
# Initial conditions
x = array([2., 0.])
x_log = [copy(x)]
k1 = 50
k2 = 5
for t in time:
    y = sense(x)
    #u = control(t, y)  
    u = PIcontrol(t,y)
    u = wind(u)
    x = simulate(Δt, x, u)
    x_log.append(copy(x))
    
x_log = array(x_log)
grid()
plot(x_log[:,0], x_log[:,1])
