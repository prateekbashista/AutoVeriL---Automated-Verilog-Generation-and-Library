module mux(input [31:0]in0  ,input [31:0]in1  ,input [31:0]in2  ,input [31:0]in3  ,input [31:0]in4  ,input [31:0]in5  ,input [31:0]in6  ,input [31:0]in7  ,input [31:0]in8  ,input [31:0]in9  ,input [31:0]in10  ,input [31:0]in11  ,input [31:0]in12  ,input [31:0]in13  ,input [31:0]in14  ,input [31:0]in15  ,input [3:0] sel, output reg [31:0]ans);

	always @(*) begin 
		 case(sel)
		 4'd0 : ans  = in0;
		 4'd1 : ans  = in1;
		 4'd2 : ans  = in2;
		 4'd3 : ans  = in3;
		 4'd4 : ans  = in4;
		 4'd5 : ans  = in5;
		 4'd6 : ans  = in6;
		 4'd7 : ans  = in7;
		 4'd8 : ans  = in8;
		 4'd9 : ans  = in9;
		 4'd10 : ans  = in10;
		 4'd11 : ans  = in11;
		 4'd12 : ans  = in12;
		 4'd13 : ans  = in13;
		 4'd14 : ans  = in14;
		 4'd15 : ans  = in15;
		 default : ans = 4'd0;
		endcase
	end

endmodule