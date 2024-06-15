import math as mt
import sys
import time


## Generating Mux Code
def mux(mux_len : int, width : int):
    sel_line = mt.log2(mux_len)
    f.write("module mux(")
    for i in range(mux_len) :
        f.write("input [" + str(width-1)+ ":0]"+ "in" + str(i) + "  ,")
    f.write("input " + "[" + str(int(sel_line-1)) + ":0] sel,")
    f.write(" output reg [" + str(width-1)+ ":0]" + "ans);")
    f.write("\n\n")

    f.write("\talways @(*) begin \n")
    f.write("\t\t case(sel)")
    for i in range(mux_len) :
        f.write("\n\t\t " + str(int(sel_line)) + "'d" + str(i) + " : ans  = in" + str(i) + ";")
    f.write("\n\t\t default : ans = " + str(int(sel_line)) +  "'d0;")
    f.write("\n\t\tendcase")
    f.write("\n\tend\n")
    f.write("\nendmodule")

def half_add() :
    f.write("module half_add(input a, input b, output s, output cout); \n\n")
    f.write("assign s = a ^ b;\n")
    f.write("assign s = a & b;\n")
    f.write("endmodule")

ip_logic = sys.argv[1]


curr = time.localtime()
f = open("../generated_verilog/"+ ip_logic + str(curr.tm_hour) + str(curr.tm_min) + str(curr.tm_sec) + ".v", "w")


##IP SELECT FOR DIFFERENT KINDS OF DIGITAL LOGIC
if ip_logic == 'mux':  
    data_width  = int(sys.argv[2])
    pins = int(sys.argv[3]) 
    mux(pins,data_width)
elif ip_logic == 'half_addr' :
    half_add()

f.close()




