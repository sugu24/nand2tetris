class CodeWriter:
    def __init__(self, output_file_name):
        self.output_file = open('{}'.format(output_file_name), "w")
        self.file_name = ""
        self.EQ = 0
        self.GT = 0
        self.LT = 0
        self.ReturnAddress = 0



    def writeInit(self):
        self.output_file.write("@256\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@SP\n")
        self.output_file.write("M=D\n")
        self.writeCall("Sys.init", "0")


    def setFileName(self, file_name):
        vm_file_name = ""
        for c in file_name[::-1]:
            if c == "/" or c == "\\":break
            vm_file_name = c + vm_file_name
        if self.file_name != vm_file_name:
            self.file_name = vm_file_name

    
    def writeArithmetic(self, command):
        if command == "add":
            self.output_file.write("// add\n")
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=M+D\n")
        elif command == "sub":
            self.output_file.write("// sub\n")
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=M-D\n")
        elif command == "neg":            
            self.output_file.write("// neg\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-M\n")
        elif command == "and":
            self.output_file.write("// and\n")
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=M&D\n")
        elif command == "or":
            self.output_file.write("// or\n")
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=M|D\n")
        elif command == "not":
            self.output_file.write("// not\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=!M\n")
        elif command == "eq":
            self.output_file.write("// eq\n")
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("D=M-D\n")

            self.output_file.write("@EQ"+str(self.EQ)+"\n")
            self.output_file.write("D;JEQ\n")

            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=0\n")
            self.output_file.write("@PROCESS"+str(self.EQ+self.GT+self.LT)+"\n")
            self.output_file.write("0;JMP\n")

            self.output_file.write("(EQ"+str(self.EQ)+")\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-1\n")
            self.output_file.write("@PROCESS"+str(self.EQ+self.GT+self.LT)+"\n")
            self.output_file.write("0;JMP\n")
            
            self.output_file.write("(PROCESS"+str(self.EQ+self.GT+self.LT)+")\n")
            self.EQ += 1
        elif command == "gt":
            self.output_file.write("// gt\n")
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("D=M-D\n")

            self.output_file.write("@GT"+str(self.GT)+"\n")
            self.output_file.write("D;JGT\n")

            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=0\n")
            self.output_file.write("@PROCESS"+str(self.EQ+self.GT+self.LT)+"\n")
            self.output_file.write("0;JMP\n")

            self.output_file.write("(GT"+str(self.GT)+")\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-1\n")
            self.output_file.write("@PROCESS"+str(self.EQ+self.GT+self.LT)+"\n")
            self.output_file.write("0;JMP\n")
            
            self.output_file.write("(PROCESS"+str(self.EQ+self.GT+self.LT)+")\n")
            self.GT += 1
        elif command == "lt":
            self.output_file.write("// lt\n")
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("D=M-D\n")

            self.output_file.write("@LT"+str(self.LT)+"\n")
            self.output_file.write("D;JLT\n")

            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=0\n")
            self.output_file.write("@PROCESS"+str(self.EQ+self.GT+self.LT)+"\n")
            self.output_file.write("0;JMP\n")

            self.output_file.write("(LT"+str(self.LT)+")\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-1\n")
            self.output_file.write("@PROCESS"+str(self.EQ+self.GT+self.LT)+"\n")
            self.output_file.write("0;JMP\n")
            
            self.output_file.write("(PROCESS"+str(self.EQ+self.GT+self.LT)+")\n")
            self.LT += 1
        
    
    # Dレジスタの値をPush
    def writePush(self):
        self.output_file.write("@SP\n")
        self.output_file.write("A=M\n")
        self.output_file.write("M=D\n")
        self.output_file.write("@SP\n")
        self.output_file.write("M=M+1\n")
    

    # DレジスタにPop
    def writePop(self):
        self.output_file.write("@SP\n")
        self.output_file.write("AM=M-1\n")
        self.output_file.write("D=M\n")


    def writePushPop(self, command, segment, index):
        if command == "push":
            if segment == "constant":
                self.output_file.write("// push constant " + index + "\n")
                self.output_file.write("@"+str(index)+"\n")
                self.output_file.write("D=A\n")

                self.writePush()
            elif segment == "local" or segment == "argument" or segment == "this" or segment == "that":
                if segment == "local":
                    SEGMENT = "LCL"
                elif segment == "argument":
                    SEGMENT = "ARG"
                elif segment == "this":
                    SEGMENT = "THIS"
                elif segment == "that":
                    SEGMENT = "THAT" 
                
                self.output_file.write("// push " + SEGMENT + " " + index + "\n")
                self.output_file.write("@"+SEGMENT+"\n")
                self.output_file.write("D=M\n")
                self.output_file.write("@"+str(index)+"\n")
                self.output_file.write("A=A+D\n")
                self.output_file.write("D=M\n")

                self.writePush()
            elif segment == "pointer":
                self.output_file.write("// push pointer " + index + "\n")
                if index == "0":
                    self.output_file.write("@THIS\n")
                elif index == "1":
                    self.output_file.write("@THAT\n")
                self.output_file.write("D=M\n")
                
                self.writePush()
            elif segment == "temp":
                self.output_file.write("// push temp " + index + "\n")
                index = str(5 + int(index))
                self.output_file.write("@"+index+"\n")
                self.output_file.write("D=M\n")

                self.writePush()
            elif segment == "static":
                self.output_file.write("// push static " + index + "\n")
                self.output_file.write("@"+ self.file_name + "." + index + "\n")
                self.output_file.write("D=M\n")

                self.writePush()
        
        elif command == "pop":
            if segment == "local" or segment == "argument" or segment == "this" or segment == "that":
                if segment == "local":
                    SEGMENT = "LCL"
                elif segment == "argument":
                    SEGMENT = "ARG"
                elif segment == "this":
                    SEGMENT = "THIS"
                elif segment == "that":
                    SEGMENT = "THAT" 

                self.output_file.write("// pop " + SEGMENT + " " + index + "\n")
                # @13に *(SEGMENT + index) を入れる        
                self.output_file.write("@"+index+"\n")
                self.output_file.write("D=A\n")
                self.output_file.write("@"+SEGMENT+"\n")
                self.output_file.write("D=M+D\n")
                self.output_file.write("@13\n")
                self.output_file.write("M=D\n")

                self.writePop()

                # *(SEGMENT + index) にpop
                self.output_file.write("@13\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=D\n")
            elif segment == "pointer":
                self.output_file.write("// pop pointer " + index + "\n")
                self.writePop()

                if index == "0":
                    self.output_file.write("@THIS\n")
                elif index == "1":
                    self.output_file.write("@THAT\n")
                self.output_file.write("M=D\n")
            elif segment == "temp":
                self.output_file.write("// pop temp " + index + "\n")
                self.writePop()

                index = str(5 + int(index))
                self.output_file.write("@"+index+"\n")
                self.output_file.write("M=D\n")
            elif segment == "static":
                self.output_file.write("// pop static " + index + "\n")
                self.writePop()

                self.output_file.write("@"+ self.file_name + "." + index+"\n")
                self.output_file.write("M=D\n")
    

    def writeLabel(self, label):
        self.output_file.write("// label\n")
        self.output_file.write("(" + label + ")\n")
    

    def writeGoto(self, label):
        self.output_file.write("// goto " + label + "\n")
        self.output_file.write("@" + label + "\n")
        self.output_file.write("0;JMP\n")

    
    def writeIf(self, label):
        self.output_file.write("// If-goto " + label + "\n")
        self.writePop()
        self.output_file.write("@" + label + "\n")
        self.output_file.write("D;JNE\n")


    def writeCall(self, functionName, numArgs):
        self.output_file.write("// call " + functionName + " " + numArgs + "\n")
        # push return-address
        self.output_file.write("@RETURNADDRESS" + str(self.ReturnAddress) + "\n")
        self.output_file.write("D=A\n")
        self.writePush()

        # push LCL
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.writePush()

        # push ARG
        self.output_file.write("@ARG\n")
        self.output_file.write("D=M\n")
        self.writePush()

        # push THIS
        self.output_file.write("@THIS\n")
        self.output_file.write("D=M\n")
        self.writePush()

        # push THAT
        self.output_file.write("@THAT\n")
        self.output_file.write("D=M\n")
        self.writePush()

        # ARG = SP-n-5
        # push SP-n-5
        self.output_file.write("@SP\n")
        self.output_file.write("D=M\n")
        self.writePush()
        
        self.output_file.write("@" + numArgs + "\n")
        self.output_file.write("D=A\n")
        self.writePush()
        self.output_file.write("@5\n")
        self.output_file.write("D=A\n")
        self.writePush()
        self.writeArithmetic("add")
        self.writeArithmetic("sub")

        # pop -> ARG
        self.writePop()
        self.output_file.write("@ARG\n")
        self.output_file.write("M=D\n")

        # LCL = SP
        self.output_file.write("@SP\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("M=D\n")

        # goto f
        self.writeGoto(functionName)

        # (return-address)
        self.output_file.write("(RETURNADDRESS" + str(self.ReturnAddress) + ")\n")
        self.ReturnAddress += 1


    def writeReturn(self):
        self.output_file.write("// return\n")
        # FRAME(@14) = LCL
        self.output_file.write("@LCL\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@14\n")
        self.output_file.write("M=D\n")

        # RET(@15) = *(FRAME-5)
        self.output_file.write("@14\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@5\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@15\n")
        self.output_file.write("M=D\n")

        # *ARG = pop()
        self.writePop()
        self.output_file.write("@ARG\n")
        self.output_file.write("A=M\n")
        self.output_file.write("M=D\n")

        # SP = ARG + 1
        self.output_file.write("@ARG\n")
        self.output_file.write("D=M+1\n")
        self.output_file.write("@SP\n")
        self.output_file.write("M=D\n")

        # THAT = *(FRAME-1)
        self.output_file.write("@14\n")
        self.output_file.write("A=M-1\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@THAT\n")
        self.output_file.write("M=D\n")

        # THIS = *(FRAME-2)
        self.output_file.write("@14\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@2\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@THIS\n")
        self.output_file.write("M=D\n")

        # ARG = *(FRAME-3)
        self.output_file.write("@14\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@3\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("M=D\n")

        # LCL = *(FRAME-4)
        self.output_file.write("@14\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@4\n")
        self.output_file.write("A=D-A\n")
        self.output_file.write("D=M\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("M=D\n")

        # goto RET
        self.output_file.write("@15\n")
        self.output_file.write("A=M\n")
        self.output_file.write("0;JMP\n")


    def writeFunction(self, functionName, numLocals):
        self.output_file.write("// function " + functionName + " " + numLocals + "\n")
        self.output_file.write("(" + functionName + ")\n")
        for i in range(int(numLocals)):
            self.output_file.write("// local " + str(i) + " <- 0\n")
            self.writePushPop("push", "constant", "0")


    def close(self):
        self.output_file.close()