%pylab inline
import matplotlib.pyplot as plt
import matplotlib.patches as mp
# Perfect sensor
def sense(x):
    return x
def simulate(Δt, x, u):
    x += Δt * u
    return x
# wayPoint [time, pt_x, pt_y, pVelocity_x, pvelocity_y]
w = [0,-5.,-7.,0,0],[3,10,-6,0.5,0.5],[6,10,-3,-0.2,0.2],[9,0,-3,-0.1,0.8],[11,0,6,0.8,0],[13,3,6,0,-0.5],[15,3,1,-0.8,0],[18,-1,0,0,1],[20,0,8,1,0.5],[24,9,10,0,0],[25,9,10,0,0]

k = 5
def control(t, y):
    ux = 0.
    uy = 0.
    for i in range(0,10):
        if w[i][0] <= t and t < w[i+1][0]:
            a0 = w[i][1]
            a1 = w[i][3]
            a2 = (3*w[i+1][1]-3*a0-2*a1*w[i+1][0]-w[i+1][3]*w[i+1][0])/w[i+1][0]**2
            a3 = (2*a0+(a1+w[i+1][3])*w[i+1][0]-2*w[i+1][1])/w[i+1][0]**3    
            ux = 3*a3*(t-w[i][0])**2+2*a2*(t-w[i][0])+a1+k*(a3*(t-w[i][0])**3+a2*(t-w[i][0])**2+a1*(t-w[i][0])+a0-y[0])
  
            a0 = w[i][2]
            a1 = w[i][4]
            a2 = (3*w[i+1][2]-3*a0-2*a1*w[i+1][0]-w[i+1][4]*w[i+1][0])/w[i+1][0]**2
            a3 = (2*a0+(a1+w[i+1][4])*w[i+1][0]-2*w[i+1][2])/w[i+1][0]**3
            uy = 3*a3*(t-w[i][0])**2+2*a2*(t-w[i][0])+a1+k*(a3*(t-w[i][0])**3+a2*(t-w[i][0])**2+a1*(t-w[i][0])+a0-y[1])
            return array([ux,uy])
tf = 24.9
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
