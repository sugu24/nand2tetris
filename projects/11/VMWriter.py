class VMWriter:
    def __init__(self, output_file_name):
        self.output_file = open(output_file_name, mode="w")
    
    def writePush(self, Segment, Index):
        segment = ""
        if Segment == "CONST":
            segment = "constant"
        elif Segment == "ARG":
            segment = "argument"
        elif Segment == "LOCAL":
            segment = "local"
        elif Segment == "STATIC":
            segment = "static"
        elif Segment == "THIS":
            segment = "this"
        elif Segment == "THAT":
            segment = "that"
        elif Segment == "POINTER":
            segment = "pointer"
        elif Segment == "TEMP":
            segment = "temp"
        else:
            print("error -----", Segment)
            return
        
        self.output_file.write("push " + segment + " " + str(Index) + "\n")
        return
    

    def writePop(self, Segment, Index):
        segment = ""
        if Segment == "CONST":
            segment = "constant"
        elif Segment == "ARG":
            segment = "argument"
        elif Segment == "LOCAL":
            segment = "local"
        elif Segment == "STATIC":
            segment = "static"
        elif Segment == "THIS":
            segment = "this"
        elif Segment == "THAT":
            segment = "that"
        elif Segment == "POINTER":
            segment = "pointer"
        elif Segment == "TEMP":
            segment = "temp"
        else:
            print("error ------",Segment)
            return
        
        self.output_file.write("pop " + segment + " " + str(Index) + "\n")
        return
    

    def writeArithmetic(self, command):
        self.output_file.write(command + "\n")
        return
    

    def writeLabel(self, label):
        self.output_file.write("label " + label + "\n")
        return
    

    def writeGoto(self, label):
        self.output_file.write("goto " + label + "\n")
        return
    

    def writeIf(self, label):
        self.output_file.write("if-goto " + label + "\n")
        return
    

    def writeCall(self, name, nArgs):
        self.output_file.write("call " + name + " " + str(nArgs) + "\n")
        return
    

    def writeFunction(self, name, nLocals):
        self.output_file.write("function " + name + " " + str(nLocals) + "\n")
        return
    

    def writeReturn(self):
        self.output_file.write("return\n")
        return
    

    def close(self):
        self.output_file.close()
        return