@256
D=A
@SP
M=D
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop LCL 0
@0
D=A
@LCL
D=M+D
@13
M=D
@SP
AM=M-1
D=M
@13
A=M
M=D
// label
(LOOP_START)
// push ARG 0
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push LCL 0
@LCL
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
// pop LCL 0
@0
D=A
@LCL
D=M+D
@13
M=D
@SP
AM=M-1
D=M
@13
A=M
M=D
// push ARG 0
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
AM=M-1
D=M
@SP
A=M-1
M=M-D
// pop ARG 0
@0
D=A
@ARG
D=M+D
@13
M=D
@SP
AM=M-1
D=M
@13
A=M
M=D
// push ARG 0
@ARG
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// If-goto LOOP_START
@SP
AM=M-1
D=M
@LOOP_START
D;JNE
// push LCL 0
@LCL
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
