# -*- coding: utf-8 -*-

# - Methods Imported - #
from matplotlib import pyplot as plt
import numpy as np

class run:
    
    def __init__(self):
        
        self.Hlib = self.lib()

        self.x = []
        self.y = []
        self.step = 0
        self.Mv = []      # Max Values
        self.MSu = []     # Max Steps Used
        self.Ms = []      # Most Stable
    
    # Pubilc    
    def Singal(self, i, m=False):
        i = int(i)
        self.__resin = i
        self.__init__()
        self.x.append(self.step)
        self.y.append(i)
        while i >= 2:
            i = self.Hlib.ParCal(i)
            self.step += 1
            self.x.append(self.step)
            self.y.append(i)
        if m == False:
            var = '{:.3f}'.format(np.var(self.y))
            plt.title(f'Singal Number {self.__resin}',loc='left')
            plt.xlabel(f'Max Value Index : {self.x[self.y.index(max(self.y))]} # {len(self.x)-1} Steps Used',loc='left')
            plt.ylabel(f'Max Value : {max(self.y)} # Variance : {var}',loc='bottom')
            self(self.x,self.y)
            plt.show()
        else:
            self.Mv.append(max(self.y))
            self.MSu.append(max(self.x))
            self.Ms.append(int(np.var(self.y)))
    
    def Multi(self,n1,n2):
        n1 = int(n1)
        n2 = int(n2)
        plt.suptitle(f'Multiple number {n1} to {n2}')
        
        # Area 1
        plt.subplot(221)
        plt.title('All Numbers',loc='left')
        for l in range(n1,n2+1):
            self.step = l
            self.Singal(l,m=True)
            self(self.x,self.y)
        
        # Area 2
        plt.subplot(222)
        self.Mv = []
        self.Ms = []
        self.MSu = []
        self.__Count = []
        for l in range(n1,n2+1):
            self.step = 0
            self.__Count.append(l)
            self.Singal(l,m=True)
        plt.title(f'Max Value {self.__Count[self.Mv.index(max(self.Mv))]} # {max(self.Mv)}',loc='left')
        self.step = 0
        self.Singal(self.__Count[self.Mv.index(max(self.Mv))],m=True)
        self(self.x,self.y)
        
        # Area 3
        plt.subplot(223)
        plt.xlabel(f'Max Steps {self.__Count[self.MSu.index(max(self.MSu))]} # {max(self.MSu)}',loc = 'left')
        self.step = 0
        self.Singal(self.__Count[self.MSu.index(max(self.MSu))],m=True)
        self(self.x,self.y)
        
        # Area 4
        plt.subplot(224)
        plt.xlabel(f'Min Variance {self.__Count[self.Ms.index(min(self.Ms))]} # {min(self.Ms)}',loc = 'left')
        self.step = 0
        self.Singal(self.__Count[self.Ms.index(min(self.Ms))],m=True)
        self(self.x,self.y)

        plt.show()
    
    class lib():
    
        def ParCal(self,i):
            if ( i % 2 ) == 0:
                Re = i / 2
                return Re
            else:
                Re = i * 3 + 1
                return Re
            
        def plot(self,a,b):
            plt.grid()
            plt.plot(a,b,'#BF514E',marker='s')