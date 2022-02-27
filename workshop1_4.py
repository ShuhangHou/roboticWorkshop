%pylab inline
import matplotlib.pyplot as plt
import matplotlib.patches as mp
# Perfect sensor
def sense(x):
    return x
def simulate(Δt, x, u):
    x += Δt * u
    return x
def control(t, y):
    ### WRITE YOUR CONTROL POLICY HERE:
    ux = 0
    uy = 0
    if t<1:
        ux = 15
        uy = 0
    elif t<2:
        ux = 0
        uy = 4
    elif t<3:
        ux = -10
        uy = 0
    elif t<4:
        ux = 0
        uy = 9
    elif t<5:
        ux = 3
        uy = 0
    elif t<6:
        ux = 0
        uy = -5
    elif t<7:
        ux = -4
        uy = 0
    elif t<8:
        ux = 0
        uy = 9
    elif t<9:
        ux = 10
        uy = 0
    return array([ux, uy])
tf = 9.
Δt = 0.1    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval

plt.figure()
rec1 = mp.Rectangle((4.0,-1.0),2,10)
rec2 = mp.Rectangle((0.5,2),2,3)
rec3 = mp.Rectangle((-6.0,-5.0),15,1)
rec4 = mp.Rectangle((8.0,0.0),2,5)
rec5 = mp.Rectangle((-4.0,-3.0),2,8)
plt.gca().add_patch(rec1)
plt.gca().add_patch(rec2)
plt.gca().add_patch(rec3)
plt.gca().add_patch(rec4)
plt.gca().add_patch(rec5)

# Initial conditions
x = array([-5., -7.])
x_log = [copy(x)]

for t in time:
    y = sense(x)
    u = control(t, y)    
    x = simulate(Δt, x, u)
    x_log.append(copy(x))
    
x_log = array(x_log)
grid()
plot(x_log[:,0], x_log[:,1])
