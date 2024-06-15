# generation of full adder code

def full_add (f):
    f.write("module full_add(input a, input b, input cin, output sum, output cout); \n\n")
    f.write("assign sum = a ^ b ^ cin;\n")
    f.write("assign cout = a&b|b&cin|a&cin;\n")
    f.write("endmodule")
