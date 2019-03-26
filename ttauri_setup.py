import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math as m
from threading import Thread

#p1 = threading.Thread(target=taskA, args=(*args, **kwargs))


class Grid():
    def __init__(self,gridSize,resolution):

        N = int(gridSize / resolution)
        self.nCells = N**3


        self.pos = np.zeros((N,N,N,3))
        self.rho = np.zeros((N,N,N))
        self.vel = np.zeros((N,N,N,3))
        self.inflow = np.full((N,N,N),False)
        self.source = np.full((N,N,N),False)
        self.temp = np.zeros((N,N,N))

        centre = 0.5 * N * resolution


        def fill_pos(self,comp):
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.pos[i,j,k,comp] = (i * resolution) - centre



        def init_thread(self,comp):
            return Thread(target=fill_pos, args=(self,comp,))
        threads = [init_thread(self,comp) for comp in range(3)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()



class Ttauri(Grid):
    def __init__(self):
        stellarRadius = 695510 #km
        AU = 149597870.7 #km
        solarMass = 1.989e30

        self.ttaurimag = True            #! with a magnetosphere
        #self.usehartmanntemp = True      #! use Hartmann's temperature distribution

        self.ttauriRstar = 2.0 * stellarRadius / AU         #! radius of the star (solar radii)
        self.ttauriMstar = 0.5 * solarMass                        #! mass of the star
        self.ttauriRinner = 2.2 * self.ttauriRstar       #! inner radius of magnetosphere (in stellar radii)
        self.holeRadius = 2.2 * self.ttauriRstar         #! put a geometrically thin, optically thick disc in the midplane
        self.ttauriRouter = 3.0 * self.ttauriRstar       #! outer radius of magnetosphere
        self.dipoleOffset = 0.0
        self.mdotpar = 1.0e-8

        self.gridSize = 1 #au
        self.resolution = 0.01 #au
        Grid.__init__(self,self.gridSize,self.resolution)
        print("Number of cells =", self.nCells)


    def createSource(self):
        thisRho = self.ttauriMstar / (1.333*m.pi*self.ttauriRstar**3)
        data = np.zeros((self.nCells,3))
        count = 0

        for cell in np.ndindex(self.rho.shape):
            r = Ttauri.modulus(self,cell)
            data[count,0] = self.pos[cell+(0,)]
            data[count,1] = self.pos[cell+(2,)]
            if(r <= self.ttauriRstar):
                self.source[cell] = True
                self.rho[cell] = thisRho
                self.temp[cell] = 40000.
                data[count,2] = thisRho
            count += 1
        return (self.pos,self.rho)



    def modulus(self,cell):
        r = 0.0
        for i in range(3):
            r += self.pos[cell+(i,)]**2
        return m.sqrt(r)




pos,rho = Ttauri().createSource()

x=pos[:,0,5,0]
y=pos[0,:,5,0]
z=rho[:,:,5]

plt.imshow(rho[:,:,50])

# plt.scatter(x,y,c=z)
plt.show()
# x = pos[:,0,0,0]
# y = pos[:,0,0,1]
# z = pos[:,0,0,2]
# print(rho)
# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')
# ax.scatter(x,y,z)
# plt.show()
