module mux(input a, input b, input sel, output ans);

assign ans = sel ? a : b;

endmodule