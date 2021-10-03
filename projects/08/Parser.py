class Parser:
    def __init__(self, input_file_name):
        self.vm_commands = []
        self.focus_line = 0
        self.focus_vm_commands = ""
        with open(input_file_name, mode='r') as f:
            for s in f:
                self.vm_commands.append(s)
        
        self.commands = [("add", "C_ARITHMETIC"),\
                   ("sub", "C_ARITHMETIC"),\
                   ("neg", "C_ARITHMETIC"),\
                   ("eq", "C_ARITHMETIC"),\
                   ("gt" ,"C_ARITHMETIC"),\
                   ("lt", "C_ARITHMETIC"),\
                   ("and", "C_ARITHMETIC"),\
                   ("or", "C_ARITHMETIC"),\
                   ("not", "C_ARITHMETIC"),\
                   ("push", "C_PUSH"),\
                   ("pop", "C_POP"),\
                   ("label", "C_LABEL"),\
                   ("goto", "C_GOTO"),\
                   ("if-goto", "C_IF"),\
                   ("function", "C_FUNCTION"),\
                   ("return", "C_RETURN"),\
                   ("call", "C_CALL")]
    

    def hasMoreCommands(self):
        if len(self.vm_commands) > self.focus_line:
            return True
        else:
            return False
    

    def advance(self):
        self.focus_vm_commands = ""
        for c in self.vm_commands[self.focus_line]:
            if ord(c) == 47:break
            self.focus_vm_commands += c
        self.focus_line += 1
        self.args = list(map(str, self.focus_vm_commands.split()))
    

    def commandType(self):
        for command, response in self.commands:
            if self.args[0] == command:
                return response
        return None


    def arg1(self):
        if len(self.args) > 0:
            return self.args[0]
        else:
            return None


    def arg2(self):
        if len(self.args) > 1:
            return self.args[1]
        else:
            return None

    def arg3(self):
        if len(self.args) > 2:
            return self.args[2]
        else:
            return None