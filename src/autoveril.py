from mux import mux
from half_add import half_add
from full_add import full_add
import sys
import time

def help():
    print("WELCOME TO AUTOVERIL \n\tHELP MENU:")
    print("\t1. mux <data_width> <number of inputs> : generates mux of specified data width and num of inputs")
    print("\t2. half_addr : generates a generic half adder")
    print("\t3. full_addr : generates a generic full adder")

ip_dict  = {
    "help" : "help",
    "mux" : "mux",
    "half_addr" : "half_addr",
    "full_addr" : "full_addr"
 }

ip_logic = sys.argv[1]

curr = time.localtime()

if ip_logic != 'help' and ip_dict.get(ip_logic) != None:
    f = open("../generated_verilog/"+ ip_logic +"_"+ str(curr.tm_hour)+"_" + str(curr.tm_min)+ "_" + str(curr.tm_sec) + ".v", "w")


##IP SELECT FOR DIFFERENT KINDS OF DIGITAL LOGIC

if ip_logic == 'help':
    help()
elif ip_logic == 'mux':  
    data_width  = int(sys.argv[2])
    pins = int(sys.argv[3]) 
    mux(f,pins,data_width)
elif ip_logic == 'half_addr' :
    half_add(f)
elif ip_logic == 'full_addr' :
    full_add(f)
else :
    help()


if ip_logic != 'help'and ip_dict.get(ip_logic) != None:
    f.close()




