# f = open("../generated_verilog/mux.v", "w")
# f.write("module mux(input a, input b, input sel, output ans);")
# f.write("\n")
# f.write("\n")
# f.write("assign ans = sel ? a : b;")
# f.write("\n")
# f.write("\n")
# f.write("endmodule")
# f.close()
import math as mt
import sys

def mux(mux_len : int, width : int):
    sel_line = mt.log2(mux_len)
    f = open("../generated_verilog/mux.v", "w")
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
    f.close()


mux(16,32)

