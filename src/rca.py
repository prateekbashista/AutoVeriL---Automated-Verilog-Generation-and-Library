import math as mt
from full_add import full_add

def rca(f, dw):
    full_add(f)
    f.write("\n\nmodule  RCA #(parameter WIDTH = " + str(dw) + ")(")
    f.write("input [WIDTH-1 : 0] a, input [WIDTH-1 : 0] b, input cin, output [WIDTH-1:0] sum, output cout);")
    f.write("\n wire [WIDTH-1:0] couts;")
    f.write("\n genvar i;")
    f.write("\n\n full_add fa0(a[0],b[0],cin,sum[0],couts[0]);")
    f.write("\n generate \n for(i = 1; i<WIDTH; i =i+1) begin")
    f.write("\n full_add FA(a[i],b[i],couts[i-1],sum[i],couts[i]); \n end \n endgenerate")
    f.write("\n assign cout = couts[WIDTH-1];")
    f.write("\nendmodule")

