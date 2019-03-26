import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from math import sqrt
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
        self.ttaurimag = True            #! with a magnetosphere
        self.ttaurirstar = 2.         #! radius of the star (must be the same as radius1)
        self.ttaurimstar = 0.5        #! mass of the star
        self.ttauririnner = 2.2       #! inner radius of magnetosphere (in stellar radii)
        self.holeradius = 2.2         #! put a geometrically thin, optically thick disc in the midplane
        self.ttaurirouter = 3.0        #! outer radius of magnetosphere
        self.dipoleoffset = 0.0       #! no dipole offset (can't do anything else in 2d)
        self.usehartmanntemp = True      #! use Hartmann's temperature distribution
        self.mdotpar = 1.0e-8


        self.gridSize = 75 #au
        self.resolution = 5 #au
        Grid.__init__(self,self.gridSize,self.resolution)
        print("Number of cells =", self.nCells)


    def createSource(self):
        for cell in np.ndindex(self.rho.shape):
            pass
            Ttauri.modulus(self,cell)
            #print(cell,self.rho[cell])


    def modulus(self,cell):
        r = 0.0
        for i in range(3):
            r += self.pos[cell+(i,)]**2
        r = sqrt(r)




x = Ttauri().createSource()

# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')
# ax.scatter(x[:,0],x[:,1],x[:,2])
# plt.show()
