class Code:
    def dest(self, mnemonic):
        if mnemonic is None: return "000"
        mnemonic_set = set(list(mnemonic))
        if len(mnemonic_set) == 3:
            if 'A' in mnemonic_set and 'M' in mnemonic_set and 'D' in mnemonic_set:
                return "111"
        elif len(mnemonic_set) == 2:
            if 'A' in mnemonic_set and 'D' in mnemonic_set:
                return "110"
            elif 'A' in mnemonic_set and 'M' in mnemonic_set:
                return "101"
            elif 'M' in mnemonic_set and 'D' in mnemonic_set:
                return "011"
        elif len(mnemonic_set) == 1:
            if 'A' in mnemonic_set:
                return "100"
            elif 'M' in mnemonic_set:
                return "001"
            elif 'D' in mnemonic_set:
                return "010"
        return None
    

    def comp(self, mnemonic):
        if mnemonic == "0":
            return "101010"
        elif mnemonic == "1":
            return "111111"
        elif mnemonic == "-1":
            return "111010"
        elif mnemonic == "D":
            return "001100"
        elif mnemonic == "A" or mnemonic == "M":
            return "110000"
        elif mnemonic == "!D":
            return "001101"
        elif mnemonic == "!A" or mnemonic == "!M":
            return "110001"
        elif mnemonic == "-D":
            return "001111"
        elif mnemonic == "-A" or mnemonic == "-M":
            return "110011"
        elif mnemonic == "D+1":
            return "011111"
        elif mnemonic == "A+1" or mnemonic == "M+1":
            return "110111"
        elif mnemonic == "D-1":
            return "001110"
        elif mnemonic == "A-1" or mnemonic == "M-1":
            return "110010"
        elif mnemonic == "D+A" or mnemonic == "A+D" or mnemonic == "D+M" or mnemonic == "M+D":
            return "000010"
        elif mnemonic == "D-A" or mnemonic == "D-M":
            return "010011"
        elif mnemonic == "A-D" or mnemonic == "M-D":
            return "000111"
        elif mnemonic == "D&A" or mnemonic == "A&D" or mnemonic == "D&M" or mnemonic == "M&D":
            return "000000"
        elif mnemonic == "D|A" or mnemonic == "A|D" or mnemonic == "D|M" or mnemonic == "M|D":
            return "010101"
        else:
            return None


    def jump(self, mnemonic):
        if mnemonic == "JGT":
            return "001"
        elif mnemonic == "JEQ":
            return "010"
        elif mnemonic == "JGE":
            return "011"
        elif mnemonic == "JLT":
            return "100"
        elif mnemonic == "JNE":
            return "101"
        elif mnemonic == "JLE":
            return "110"
        elif mnemonic == "JMP":
            return "111"
        elif mnemonic is None:
            return "000"
        else:
            return None