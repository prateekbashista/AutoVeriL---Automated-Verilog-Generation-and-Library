# generation of half adder module
def half_add(f) :
    f.write("module half_add(input a, input b, output sum, output cout); \n\n")
    f.write("assign sum = a ^ b;\n")
    f.write("assign cout = a & b;\n")
    f.write("endmodule")