# -*- coding: utf-8 -*-

# - Funtions Imported - #
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

class pylight:
    
    __virsion__ = 0.5
    
    # Methods
    def light (self, loc, inte, size, pltshow=False, datashow=False, colormap='default'):
                   # Location, Intensity
             
        # Value Check

        if isinstance(loc,list) != True:
            raise ValueError(
                f"object '{loc}' is not a supposted type. supposted type: 'list'"
)
        elif isinstance(size,list) != True:
            raise ValueError(
                f"bject '{size}' is not a supposted type. supposted type: 'list'"
)
        elif len(loc) != 2:
            raise IndexError(
                f"list 'loc' length can be only be 2, not {len(loc)}"
)
        elif len(size) != 2:
            raise IndexError(
                f"list 'size' length can be only be 2, not {len(size)}"
)
        elif size[0] != size[1]:
            raise ValueError(
                'Well...I will add this funtion soon... probably;)'
)
        try:
            int(inte)
        except ValueError:
            raise ValueError(
                f"attribute 'inte' can be only integer, not '{inte}'"
)
        self.size = size
        self.debug = datashow
        self.pltshow = pltshow

        self.data = np.zeros(shape=size)
        self.datac = np.zeros(shape=size)
        
        self.data[loc[0]-1:loc[0],loc[1]-1:loc[1]] = 1.
        self.datac[loc[0]-1:loc[0],loc[1]-1:loc[1]] = 1.
        self.dinte = np.linspace(1,0,inte+1)
        
        for i in range(0,2):
            self.__rad()
            self.__dflip()

        if self.debug == True:
            print(f'data:\n{self.data}')
            print(f'datac:\n{self.datac}')

        if self.pltshow == True:
            if 0 not in self.data and self.debug == False:
                print(
                    "There are no Backround color on your map, use the 'debug' attribute to check it"
)
            colors = [
                '#000000', # Sakura Pink
                '#FFFF00'  # Maple Red
]
            cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)  
            plt.imshow(self.data,cmap=cmap)
            if self.debug == True:
                plt.colorbar()
            plt.show()
        
    def __rad(self):
        for l in range(0,self.size[1]):
            count = -1
            for i in self.data[l]:
                count += 1
                if self.datac[l,count] == 1:
                    pass
                else:
                    add = []
                    cadd = False
                    try:
                        if self.data[l,count+1] in self.dinte and self.data[l,count+1] != 0:
                            cadd = True
                            add.append(self.dinte[np.argwhere(self.dinte==self.data[l,count+1])+1])
                    except:
                        pass
                    try:
                        if self.data[l,count-1] in self.dinte and self.data[l,count-1] != 0:
                            cadd = True
                            add.append(self.dinte[np.argwhere(self.dinte==self.data[l,count-1])+1])
                    except:
                        pass
                    try:
                        if self.data[l-1,count] in self.dinte and self.data[l-1,count] != 0:
                            cadd = True
                            add.append(self.dinte[np.argwhere(self.dinte==self.data[l-1,count])+1])
                    except:
                        pass
                    try:
                        if self.data[l+1,count] in self.dinte and self.data[l+1,count] != 0:
                            cadd = True
                            add.append(self.dinte[np.argwhere(self.dinte==self.data[l+1,count])+1])
                    except:
                        pass
                    try:
                        self.data[l,count] = max(add)
                    except:
                        pass
                    if cadd == True:
                        self.datac[l,count] = 1
            
    def __dflip(self):
        
        np.flip(self.data,axis=0)
        np.flip(self.data,axis=1)
        np.flip(self.datac,axis=0)
        np.flip(self.datac,axis=1)

#if __name__ == '__main__':
f = pylight()
f.light([3,3],20,[50,50],pltshow=True,datashow=True)
    