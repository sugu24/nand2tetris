class SymbolTable:
    def __init__(self):
        self.static_symbol_table = dict()
        self.field_symbol_table = dict()
        self.arg_symbol_table = dict()
        self.var_symbol_table = dict()
    

    def startSubroutine(self):
        self.arg_symbol_table = dict()
        self.var_symbol_table = dict()
    

    def define(self, name, type, kind):
        if kind == "STATIC":
            if name not in self.static_symbol_table:
                self.static_symbol_table[name] = (type, len(self.static_symbol_table))
        elif kind == "FIELD":
            if name not in self.field_symbol_table:
                self.field_symbol_table[name] = (type, len(self.field_symbol_table))
        elif kind == "ARG":
            if name not in self.arg_symbol_table:
                self.arg_symbol_table[name] = (type, len(self.arg_symbol_table))
        elif kind == "VAR":
            if name not in self.var_symbol_table:
                self.var_symbol_table[name] = (type, len(self.var_symbol_table))
            

    def varCount(self, kind):
        if kind == "STATIC":
            return len(self.static_symbol_table)
        elif kind == "FIELD":
            return len(self.field_symbol_table)
        elif kind == "ARG":
            return len(self.arg_symbol_table)
        elif kind == "VAR":
            return len(self.var_symbol_table)
    

    def kindOf(self, name):
        if name in self.var_symbol_table:
            return "VAR"
        elif name in self.arg_symbol_table:
            return "ARG"
        elif name in self.field_symbol_table:
            return "FIELD"
        elif name in self.static_symbol_table:
            return "STATIC"
        else:
            return None
    

    def typeOf(self, name):
        # 大文字
        if name in self.var_symbol_table:
            (type, _) = self.var_symbol_table[name]
            return type
        elif name in self.arg_symbol_table:
            (type, _) = self.arg_symbol_table[name]
            return type
        elif name in self.field_symbol_table:
            (type, _) = self.field_symbol_table[name]
            return type
        elif name in self.static_symbol_table:
            (type, _) = self.static_symbol_table[name]
            return type
        else:
            return None
    

    def indexOf(self, name):
        if name in self.var_symbol_table:
            (_, index) = self.var_symbol_table[name]
            return index
        elif name in self.arg_symbol_table:
            (_, index) = self.arg_symbol_table[name]
            return index
        elif name in self.field_symbol_table:
            (_, index) = self.field_symbol_table[name]
            return index
        elif name in self.static_symbol_table:
            (_, index) = self.static_symbol_table[name]
            return index
        else:
            return None