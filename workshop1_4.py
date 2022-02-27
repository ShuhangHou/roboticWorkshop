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
    return array([ux, uy])
tf = 7.
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
x = array([3+3**0.5, 2.5])
x_log = [copy(x)]

for t in time:
    y = sense(x)
    u = control(t, y)    
    x = simulate(Δt, x, u)
    x_log.append(copy(x))
    
x_log = array(x_log)
grid()
plot(x_log[:,0], x_log[:,1])
