module mux(input [15:0]in0  ,input [15:0]in1  ,input [15:0]in2  ,input [15:0]in3  ,input [1:0] sel, output reg [15:0]ans);

	always @(*) begin 
		 case(sel)
		 2'd0 : ans  = in0;
		 2'd1 : ans  = in1;
		 2'd2 : ans  = in2;
		 2'd3 : ans  = in3;
		 default : ans = 2'd0;
		endcase
	end

endmodule