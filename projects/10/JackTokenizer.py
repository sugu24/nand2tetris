class JackTokenizer:
    from collections import deque
    def __init__(self, input_file):
        self.jack_commands = self.deque([])
        self.focus_token = ""
        self.used = True
        self.keyword_set = set(["class", "constructor", "function", "method", "field",\
            "static", "var", "int", "char", "boolean", "void", "true", "false",\
            "null", "this", "let", "do", "if", "else", "while", "return"])
        self.symbol_set = set(["{", "}", "(", ")", "[", "]", ".", ",", ";", "+", "-", "*", "/", "&",\
            "|", "<", ">", "=", "~"])

        with open(input_file, mode="r") as f:
            comment = False
            for s in f:
                i = 0
                while i < len(s):
                    # // 
                    if len(s) > i+1 and s[i] == "/" and s[i+1] == "/":
                        break
                    # /*
                    if len(s) > i+1 and s[i] == "/" and s[i+1] == "*":
                        comment = True
                    # */ (/* ... *(改行)/ は検知できない)
                    if len(s) > i+1 and s[i] == "*" and s[i+1] == "/":
                        comment = False
                        i += 2
                        continue
                    if not comment:
                        self.jack_commands.append(s[i])
                    i += 1
    

    def hasMoreTokens(self):
        if len(self.jack_commands) > 0:
            return True
        else:
            return False


    def advance(self):
        if not self.used: return
        self.focus_token = ""
        string = False
        self.used = False
        while len(self.jack_commands) > 0:
            c = self.jack_commands.popleft()
            # int_const or identifier (空白 or 改行)
            if (not string) and (ord(c) == 10 or ord(c) == 32 or ord(c) == 9):
                if len(self.focus_token) > 0:
                    return
                else:
                    continue
            
            # int_const or identifier (symbol前のトークン 例:3+)
            if (not string) and len(self.focus_token) > 0 and c in self.symbol_set:
                self.jack_commands.appendleft(c)
                return

            self.focus_token += c
            
            # symbol
            if self.focus_token in self.symbol_set:
                return
            
            # keyword
            if self.focus_token in self.keyword_set:
                return
            
            # string_const
            if self.focus_token[-1] == "\"":
                if string:
                    return
                else:
                    string = True

        # last token
        return
    

    def tokenType(self):
        if self.focus_token in self.keyword_set:
            return "KEYWORD"
        elif self.focus_token in self.symbol_set:
            return "SYMBOL"
        elif self.focus_token[0] == "\"" and self.focus_token[-1] == "\"":
            return "STRING_CONST"
        elif self.focus_token.isdigit():
            return "INT_CONST"
        else:
            return "IDENTIFIER"
    

    def keyWord(self):
        print(self.focus_token)
        self.used = True
        return self.focus_token
    

    def symbol(self):
        print(self.focus_token)
        self.used = True
        return self.focus_token
    

    def identifier(self):
        print(self.focus_token)
        self.used = True
        return self.focus_token
    

    def intVal(self):
        print(self.focus_token)
        self.used = True
        return int(self.focus_token)
    

    def stringVal(self):
        print(self.focus_token)
        self.used = True
        return self.focus_token[1:-2]
