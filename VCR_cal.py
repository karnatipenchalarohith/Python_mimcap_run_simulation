
import pandas as pd
import matplotlib.pyplot as plt

from  netlist import createnetlist as netlist
from  extract_data import extractdata as extractdata
import os


import numpy as np

from scipy.stats import linregress
from sklearn import linear_model

from  average_list import Average as Average


path_point_meas= r"/user/rkar/data_from_tp/tC18d_CMIM_update/W6C443.W16_cmim_clr/clr/"

Device_name="cmim"

filename= Device_name + '_p025.txt'

with open(path_point_meas + filename) as f:
    df = pd.read_csv(f, sep="\t", header=None)

df.columns = ["SN", "M", "W", "L", "TEMP", "V", "C"]



temperature=25

#Mult=[16,100,16,100,16,100,16,100,16,100,16,100,10,10,10,10,10,100,10,100,100,100,100,100]
#Width=[4,4,4,4,10,10,10,10,20,20,30,30,4,4,10,10,20,10,30,20,4,4,30,10]
#Length=[4,4,30,30,10,10,30,30,20,20,30,30,4,30,10,30,20,30,30,20,4,30,30,10]

Mult=[16,100,16,100,16,100,16,100,16,100,16,100]
Width=[4,4,4,4,10,10,10,10,20,20,30,30]
Length=[4,4,30,30,10,10,30,30,20,20,30,30]

#Mult=[16]
#Width=[4]
#Length=[4]


print(len(Mult))
print(len(Width))
print(len(Length))

VCR2=[]
VCR1=[]
V_coeff=[]
model_eqns=[]

for iter in range(0,len(Mult)):
    
    print(iter)
    print(Mult[iter])
    M=Mult[iter]
    W=Width[iter]
    L=Length[iter]
    
    print(M)
    print(W)
    print(L)






#    print(df)
#    M=100
#    W=10
#    L=10



    df_VCR1 = df[(df['M'] == M) & (df['W'] == W) & (df['L'] == L) & (df['SN'] == iter+1) ]



    print(df_VCR1)

    print(df_VCR1[(df_VCR1['V'] == 0)])
    df_vcr1_only=df_VCR1[(df_VCR1['V'] == 0)]

    cap_at_zero=df_vcr1_only['C'].iloc[0]
    print(df_vcr1_only['C'].iloc[0])

    #print(ff['ID'].iloc[11])


    #df_VCR1

    Cap_values =df_VCR1['C']
    Voltage=df_VCR1['V']




    #mp.scatter(Voltage,Cap_values )
    #mp.show()
    
    

    model = np.poly1d(np.polyfit(Voltage,Cap_values, 2))

    print(model)


    model2=model/df_vcr1_only['C'].iloc[0]

    print(model2)


    print(model2.c)
    model_eqns.append(model2)

    VCR2.append(model2.c[0])
    VCR1.append(model2.c[1])
    V_coeff.append(model2.c[2])
    
    lib_path ='/user/rkar/data_from_tp/tC18d_CMIM_update/all.scs'
    corner ='tt_lib'
    
    
    hertz='100k'
    Voltage_start=-10
    Voltage_stop=10
    Voltage_step=0.4

    Temp=25


    modelname ='cmim'

    terminals=2




    netlist(W, L, M, Voltage_start, Voltage_stop, Voltage_step, hertz, Temp, lib_path, corner, modelname,terminals)

    cmd=r'spectre netlist.sp +aps =log netlist1.log'
    os.system(cmd)
    
    df_sim=extractdata(Voltage_start,Voltage_stop,Voltage_step)
    
    os.remove("netlist.sp")
    os.remove("netlist.measure")
    print(df_sim)
    
    
    
    Cap_values =df_VCR1['C']
    Voltage=df_VCR1['V']
    
    corner_ss='ss_lib'
    corner_ff='ff_lib'
    
    netlist(W, L, M, Voltage_start, Voltage_stop, Voltage_step, hertz, Temp, lib_path, corner_ss, modelname,terminals)
    
    cmd=r'spectre netlist.sp +aps =log netlist1.log'
    os.system(cmd)
    
    df_sim_ss=extractdata(Voltage_start,Voltage_stop,Voltage_step)
    
    os.remove("netlist.sp")
    os.remove("netlist.measure")
    
    
    netlist(W, L, M, Voltage_start, Voltage_stop, Voltage_step, hertz, Temp, lib_path, corner_ff, modelname,terminals)
    
    cmd=r'spectre netlist.sp +aps =log netlist1.log'
    os.system(cmd)
    
    df_sim_ff=extractdata(Voltage_start,Voltage_stop,Voltage_step)
    
    os.remove("netlist.sp")
    os.remove("netlist.measure")
    
    
    aa=plt.figure()
    
    plt.plot(df_VCR1['V'], df_VCR1['C'],"s",markersize=1, color='r', label='Vb=0')
    
    
    plt.plot(df_sim['vg'], df_sim['capacitance'], color='g', label='Vb=0 TT')
    
    plt.plot(df_sim_ss['vg'], df_sim_ss['capacitance'], color='c', label='Vb=0 SS')
    
    plt.plot(df_sim_ff['vg'], df_sim_ff['capacitance'], color='m', label='Vb=0 FF')
    
    
    
    titlename=  "Number: "+ str(iter+1)  + " " +  Device_name + "  " + "W=" + str(W) + " " + "L=" + str(L) + " " + "nf=" + str(M) + "_MIMCAP vs Voltage"
    
    plt.title(titlename)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Cap (F)')
    
    plt.legend()
    plt.show()
    aa.savefig(titlename + '.png')
    
    
    
    
    print(df_VCR1)

    print(df_VCR1[(df_VCR1['V'] == 0)])
    df_vcr1_only=df_VCR1[(df_VCR1['V'] == 0)]

    cap_at_zero_meas=df_vcr1_only['C'].iloc[0]
    print(df_vcr1_only['C'].iloc[0])
    
    ab=plt.figure()
    plt.plot(df_VCR1['V'], df_VCR1['C']/cap_at_zero_meas,"s",markersize=1, color='r', label='Vb=0')
    
    df_sim_only_tt=df_sim[(df_sim['vg'] == 0)]

    cap_at_zero_tt=df_sim_only_tt['capacitance'].iloc[0]
    
   
    plt.plot(df_sim['vg'], df_sim['capacitance']/cap_at_zero_tt, color='g', label='Vb=0 TT')
    
    titlename=  "Number: " + str(iter+1) + " " +  Device_name + " " + "  " + "W=" + str(W) + " " + "L=" + str(L) + " " + "nf=" + str(M) + "_MIMCAP vs Voltage Coefficients"

    plt.title(titlename)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Normalised{Cap(F)/Cap(F) at V=0}')
    
    plt.legend()
    plt.show()
    
    ab.savefig(titlename + '.png')




print(VCR2)
print(VCR1)
print(V_coeff)
print(model_eqns)

VCR2_avg = Average(VCR2)
VCR1_avg = Average(VCR1)
V_coeff_avg = Average(V_coeff)


print(VCR2_avg)
print(VCR1_avg)
print(V_coeff_avg)

#os.remove("netlist.sp")
#os.remove("netlist.measure")
