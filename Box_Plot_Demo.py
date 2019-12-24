# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 01:18:15 2019

@author: default
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 01:03:49 2019

@author: default
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 00:36:48 2019

@author: default
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 23:08:44 2019

@author: default
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 22:26:40 2019

@author: default
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 20:52:35 2018

@author: khadak
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import matplotlib.ticker as ticker
# Set the global font to be DejaVu Sans, size 10 (or any other sans-serif font of your choice!)
rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans'],'size':10})

# Set the font used for MathJax - more on this later
rc('mathtext',**{'default':'regular'})

# Define data rate in number of packets

x = ['0.35','0.55','0.75','0.95']

parent_change = [5, 7, 18, 20]
life_time = [4, 6, 8, 10]
variance1 = [1, 2, 7, 3]
variance2=[1,2,3,4]
x_pos = [i for i, _ in enumerate(x)]


fig, axs = plt.subplots(2, 1, sharex=True, figsize=(4,5))
#fig, ax = plt.subplots(2,2)

#ax.tick_params(direction='inout', length=4, width=1, colors='black', grid_color='r', grid_alpha=0.3, labeltop='off', top=True, right=True)

axs[0].bar(x_pos, parent_change, color='#646464', yerr = variance1)        

axs[0].set_ylabel("Avg. parent change",fontname="palatino linotype", fontsize=12)
#plt.title("Parent chagne vs smoothing frequency",fontname="palatino linotype", fontsize=12)
plt.grid(axis ='both', linestyle = '--', linewidth=0.5)
plt.xticks(x_pos, x)

axs[1].bar(x_pos, life_time, color='#646464', yerr = variance2)
axs[1].set_xlabel (r'$\beta$ (smoothing factor)', fontname="palatino linotype", fontsize=12)
axs[1].set_ylabel("Average lifetime",fontname="palatino linotype", fontsize=12)

plt.xticks(x_pos, x)

plt.grid(axis ='both', linestyle = '--', linewidth=0.5)
#fig.tight_layout()

plt.show()



















































