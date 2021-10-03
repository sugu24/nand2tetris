class Parser:
    def __init__(self, input_file_name):
        self.Assemble = []
        self.focus_line = 0
        self.focus_assemble = ""
        with open(input_file_name, mode='r') as f:
            for s in f:
                self.Assemble.append(s)
    

    def hasMoreCommands(self):
        if len(self.Assemble) > self.focus_line:
            return True
        else:
            return False
    

    def advance(self):
        self.focus_assemble = ""
        for c in self.Assemble[self.focus_line]:
            asc = ord(c)
            if asc == 32 or asc == 10:continue
            if asc == 47:break
            self.focus_assemble += c
        self.focus_line += 1
    

    def commandType(self):
        if self.focus_assemble[0] == '@':
            return "A_COMMAND"
        elif self.focus_assemble[0] == '(' and self.focus_assemble[-1] == ')':
            return "L_COMMAND"
        else:
            return "C_COMMAND"
    

    def symbol(self):
        def ban(c):
            asc = ord(c)
            if 48 <= asc <= 57 or 65 <= asc <= 90 or 97 <= asc <= 122 or asc == 95 or asc == 46 or asc == 36 or asc == 58:
                return False
            return True

        symbol = self.focus_assemble[1:] if self.focus_assemble[0] == '@' else self.focus_assemble[1:-1]
        for c in symbol:
            if ban(c):
                return None
        return symbol
    

    def dest(self):
        for index, c in enumerate(self.focus_assemble):
            if c == "=":
                return self.focus_assemble[:index]
        return None
    

    def comp(self):
        for index, c in enumerate(self.focus_assemble):
            if c == "=":
                return self.focus_assemble[index+1:]
            elif c == ";":
                return self.focus_assemble[:index]
        return None
        

    def jump(self):
        for index, c in enumerate(self.focus_assemble):
            if c == ";":
                return self.focus_assemble[index+1:]
        return None