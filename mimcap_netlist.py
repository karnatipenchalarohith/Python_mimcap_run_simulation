

from  netlist import createnetlist as netlist
import os

lib_path ='/user/rkar/data_from_tp/tC18d_CMIM_update/all.scs'
corner ='tt_lib'

wt='4u'
lt='4u'
mt='100'
hertz='100k'
Voltage_start=-10
Voltage_stop=10
Voltage_step=0.4

Temp=25


modelname ='cmim'

terminals=2




netlist(wt, lt, mt, Voltage_start, Voltage_stop, Voltage_step, hertz, Temp, lib_path, corner, modelname,terminals)

cmd=r'spectre netlist.sp +aps =log netlist1.log'
os.system(cmd)





