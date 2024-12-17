# -*- coding: utf-8 -*-

# - Methods Imported - #
from matplotlib import pyplot as plt
import numpy as np
import wx

class hail:
    
    __virsion__ = '0.1b'

    # Private Values
    __x = []
    __y = []
    __St = 0
    __Mv = []      # Max Values
    __MSu = []     # Max Steps Used
    __Ms = []      # Most Stable
    
    # Pubilc
    def singal(self, i, m=False):
        i = int(i)
        self.__resin = i
        self.__x = []
        self.__y = []
        self.__x.append(self.__St)
        self.__y.append(i)
        while i >= 2:
            i = self.__ParCal(i)
            self.__St += 1
            self.__x.append(self.__St)
            self.__y.append(i)
        if m == False:
            var = '{:.3f}'.format(np.var(self.__y))
            plt.title(f'Singal Number {self.__resin}',loc='left')
            plt.xlabel(f'Max Value Index : {self.__x[self.__y.index(max(self.__y))]} # {len(self.__x)-1} Steps Used',loc='left')
            plt.ylabel(f'Max Value : {max(self.__y)} # Variance : {var}',loc='bottom')
            self.__plot(self.__x,self.__y)
            plt.show()
        else:
            self.__Mv.append(max(self.__y))
            self.__MSu.append(max(self.__x))
            self.__Ms.append(int(np.var(self.__y)))
    
    def multiple(self,n1,n2):
        n1 = int(n1)
        n2 = int(n2)
        plt.suptitle(f'Multiple number {n1} to {n2}')
        
        # Area 1
        plt.subplot(221)
        plt.title('All Numbers',loc='left')
        for l in range(n1,n2+1):
            self.__St = l
            self.singal(l,m=True)
            self.__plot(self.__x,self.__y)
        
        # Area 2
        plt.subplot(222)
        self.__Mv = []
        self.__Ms = []
        self.__MSu = []
        self.__Count = []
        for l in range(n1,n2+1):
            self.__St = 0
            self.__Count.append(l)
            self.singal(l,m=True)
        plt.title(f'Max Value {self.__Count[self.__Mv.index(max(self.__Mv))]} # {max(self.__Mv)}',loc='left')
        self.__St = 0
        self.singal(self.__Count[self.__Mv.index(max(self.__Mv))],m=True)
        self.__plot(self.__x,self.__y)
        
        # Area 3
        plt.subplot(223)
        plt.xlabel(f'Max Steps {self.__Count[self.__MSu.index(max(self.__MSu))]} # {max(self.__MSu)}',loc = 'left')
        self.__St = 0
        self.singal(self.__Count[self.__MSu.index(max(self.__MSu))],m=True)
        self.__plot(self.__x,self.__y)
        
        # Area 4
        plt.subplot(224)
        plt.xlabel(f'Min Variance {self.__Count[self.__Ms.index(min(self.__Ms))]} # {min(self.__Ms)}',loc = 'left')
        self.__St = 0
        self.singal(self.__Count[self.__Ms.index(min(self.__Ms))],m=True)
        self.__plot(self.__x,self.__y)
     
        plt.show()
    
    # Private Methods
    
    def __ParCal(self,i):
        if ( i % 2 ) == 0:
            Re = i / 2
            return Re
        else:
            Re = i * 3 + 1
            return Re
            
    def __plot(self,a,b):
        plt.grid()
        plt.plot(a,b,'#BF514E',marker='s')
    
if __name__ == '__main__':
    f = hail()
    f.singal(21)
    f.multiple(10,50)