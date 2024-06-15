import math as mt

## generation of mux module
def mux(f,mux_len : int, width : int):
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