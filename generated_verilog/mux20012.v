module mux(input [63:0]in0  ,input [63:0]in1  ,input [0:0] sel, output reg [63:0]ans);

	always @(*) begin 
		 case(sel)
		 1'd0 : ans  = in0;
		 1'd1 : ans  = in1;
		 default : ans = 1'd0;
		endcase
	end

endmodule