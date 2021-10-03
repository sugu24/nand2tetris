// function SimpleFunction.test 2
(SimpleFunction.test)
// local 0 <- 0
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// local 1 <- 0
// push constant 0
@0
D=A
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
// push LCL 1
@LCL
D=M
@1
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
// not
@SP
A=M-1
M=!M
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
// add
@SP
AM=M-1
D=M
@SP
A=M-1
M=M+D
// push ARG 1
@ARG
D=M
@1
A=A+D
D=M
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
// return
@LCL
D=M
@14
M=D
@14
D=M
@5
A=D-A
D=M
@15
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@14
A=M-1
D=M
@THAT
M=D
@14
D=M
@2
A=D-A
D=M
@THIS
M=D
@14
D=M
@3
A=D-A
D=M
@ARG
M=D
@14
D=M
@4
A=D-A
D=M
@LCL
M=D
@15
A=M
0;JMP
