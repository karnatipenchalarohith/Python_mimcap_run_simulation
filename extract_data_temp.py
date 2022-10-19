#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:47:16 2022

@author: rkar
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:57:54 2022

@author: rkar
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
#from scipy.interpolate import make_interp_spline

def extractdata_temp(temp_start,temp_stop,temp_step):
    
    starting_rub=10
    

    
    
    total_vgs_points=abs(int((temp_start-temp_stop)/temp_step))
    
        
    
        
    with open('netlist_temp.measure') as f:
        lines_after_17 = f.readlines()[starting_rub+1:starting_rub+total_vgs_points+2]
        
      
    
    
    
    print(lines_after_17)
    clean_lines=[x.strip(' ') for x in lines_after_17]
    
    
    print(clean_lines)
    
    
    Vg = []
    Cap = []
    
    for row in clean_lines:
        row=re.split(' +', row)
        #row = row.split('/s* ')
        print(row)
        
    
        Vg.append(row[3])
        Cap.append(row[5])
        
    
        x = np.array(Vg)
        Vg_full = list(map(float, x))
        y = np.array(Cap)
        cap_full = list(map(float, y))
        
            
            
    print(Vg_full)
    print(cap_full)
       
    
    
    
    print(Vg)
    print(Cap)
    
    
    
    plt.plot(Vg_full,cap_full,'b')
    
    data = {'vg': Vg_full,
           'capacitance': cap_full}

    
    df = pd.DataFrame(data)
    
    return df

'''

#print(lines_after_17)

clean_lines=[x.strip(' ') for x in lines_after_17]
clean_lines2=[x.strip(' ') for x in lines_after_17_2]
clean_lines3=[x.strip(' ') for x in lines_after_17_3]
clean_lines4=[x.strip(' ') for x in lines_after_17_4]
clean_lines5=[x.strip(' ') for x in lines_after_17_5]


print(clean_lines4)


#print(clean_lines)

Vgs = []
Ids = []
for row in clean_lines:
    row=re.split(' +', row)
    #row = row.split('/s* ')
    print(row)
    Vgs.append(row[0])
    Ids.append(row[1])
    x = np.array(Vgs)
    Vgs_fin_VB0 = list(map(float, x))
    y = np.array(Ids)
    Ids_fin_VB0 = list(map(float, y))

Vgs = []
Ids = []


for row in clean_lines2:
    row=re.split(' +', row)
    #row = row.split('/s* ')
    #print(row)
    Vgs.append(row[0])
    Ids.append(row[1])
    x = np.array(Vgs)
    Vgs_fin_VB1 = list(map(float, x))
    y = np.array(Ids)
    Ids_fin_VB1 = list(map(float, y))

Vgs = []
Ids = []


for row in clean_lines3:
    row=re.split(' +', row)
    #row = row.split('/s* ')
    #print(row)
    Vgs.append(row[0])
    Ids.append(row[1])
    x = np.array(Vgs)
    Vgs_fin_VB2 = list(map(float, x))
    y = np.array(Ids)
    Ids_fin_VB2 = list(map(float, y))

Vgs = []
Ids = []


for row in clean_lines4:
    row=re.split(' +', row)
    #row = row.split('/s* ')
    #print(row)
    Vgs.append(row[0])
    Ids.append(row[1])
    x = np.array(Vgs)
    Vgs_fin_VB3 = list(map(float, x))
    y = np.array(Ids)
    Ids_fin_VB3 = list(map(float, y))
    
Vgs = []
Ids = []

for row in clean_lines5:
    row=re.split(' +', row)
    #row = row.split('/s* ')
    #print(row)
    Vgs.append(row[0])
    Ids.append(row[1])
    x = np.array(Vgs)
    Vgs_fin_VB4 = list(map(float, x))
    y = np.array(Ids)
    Ids_fin_VB4 = list(map(float, y))


#print (x)
#print (y)

plt.plot(Vgs_fin_VB0,Ids_fin_VB0,'b')
plt.plot(Vgs_fin_VB1,Ids_fin_VB1,'b')
plt.plot(Vgs_fin_VB2,Ids_fin_VB2,'b')
plt.plot(Vgs_fin_VB3,Ids_fin_VB3,'b')
plt.plot(Vgs_fin_VB4,Ids_fin_VB4,'b')

plt.yscale('log')

plt.show()


plt.plot(Vgs_fin_VB0,Ids_fin_VB0,'b')
plt.plot(Vgs_fin_VB1,Ids_fin_VB1,'b')
plt.plot(Vgs_fin_VB2,Ids_fin_VB2,'b')
plt.plot(Vgs_fin_VB3,Ids_fin_VB3,'b')
plt.plot(Vgs_fin_VB4,Ids_fin_VB4,'b')

#plt.yscale('log')

plt.show()

data = {'vgs': Vgs_fin_VB0,
       'Ids_vb0': Ids_fin_VB0,
       'Ids_vb1': Ids_fin_VB1,
       'Ids_vb2': Ids_fin_VB2,
       'Ids_vb3': Ids_fin_VB3,
       'Ids_vb4': Ids_fin_VB4}

df = pd.DataFrame(data)

return df

'''