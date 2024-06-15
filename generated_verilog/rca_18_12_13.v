module full_add(input a, input b, input cin, output sum, output cout); 

assign sum = a ^ b ^ cin;
assign cout = a&b|b&cin|a&cin;
endmodule

module  RCA #(parameter WIDTH = 5)(input [WIDTH-1 : 0] a, input [WIDTH-1 : 0] b, input cin, output [WIDTH-1:0] sum, output cout);
 wire [WIDTH-1:0] couts;
 genvar i;

 full_add fa0(a[0],b[0],cin,sum[0],couts[0]);
 generate 
 for(i = 1; i<WIDTH; i =i+1) begin
 full_add FA(a[i],b[i],couts[i-1],sum[i],couts[i]); 
 end 
 endgenerate
 assign cout = couts[WIDTH-1];
endmodule