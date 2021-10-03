class CompilationEngine:
    import JackTokenizer, VMWriter, SymbolTable
    def __init__(self, input_file, output_file):
        self.jack_tokenizer = self.JackTokenizer.JackTokenizer(input_file)
        self.vm_writer = self.VMWriter.VMWriter(output_file)
        self.symbol_table = self.SymbolTable.SymbolTable()
        self.file_name = ""
        for c in input_file[-6::-1]:
            if ord(c) == 92 or ord(c) == 47:
                break
            self.file_name = c + self.file_name
        
        # label
        self.if_label = 0
        self.while_label = 0

        # dfs start
        self.compileClass()

    

    def compileClass(self):
        # class
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "class":
                token = self.jack_tokenizer.keyWord()
            else:
                print(1)
        else:
            return
        
        # class名
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                self.class_name = self.jack_tokenizer.identifier()
            else:
                print(3)
        else:
            return

        # <symbol> { </symbol>
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL":
                token = self.jack_tokenizer.symbol()
            else:
                print(4)
        else:
            return

        # classVarDec*
        while True:
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "static" or self.jack_tokenizer.focus_token == "field"):
                    self.compileClassVarDec()
                else:
                    break
            else:
                print(6)
        
        # subroutineDec*
        while True:
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "constructor" or self.jack_tokenizer.focus_token == "function" or self.jack_tokenizer.focus_token == "method"):
                    self.compileSubroutine()
                else:
                    break
            else:
                print(16)
        
        # <symbol> } </symbol>
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL":
                token = self.jack_tokenizer.symbol()
            else:
                print(5)
        else:
            return
        
        # ファイルを閉じる
        self.vm_writer.close()
    


    def compileClassVarDec(self):
        # static field
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "static" or self.jack_tokenizer.focus_token == "field"):
                kind = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(6)
        
        # type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                type = self.jack_tokenizer.keyWord()
            elif token_type == "IDENTIFIER":
                type = self.jack_tokenizer.identifier()
            else:
                print(7)
        else:
            print(8)
        
        # varName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                name = self.jack_tokenizer.identifier()
            else:
                print(9)
        else:
            print(10)
        
        # symbol define
        self.symbol_table.define(name, type, kind)

        # (, varName)*
        while True:
            # ,
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ",":
                    token = self.jack_tokenizer.symbol()
                else:
                    # , 以外はbreak
                    break
            else:
                print(11)
            
            # varName
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "IDENTIFIER":
                    name = self.jack_tokenizer.identifier()
                else:
                    print(12)
            else:
                print(13)
            
            # symbol define
            self.symbol_table.define(name, type, kind)
        
        # ; 
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                token = self.jack_tokenizer.symbol()
            else:
                print(14)
        else:
            print(15)
        
        return
    

    def compileSubroutine(self):
        # sybroutineの初め
        self.symbol_table.startSubroutine()

        # constructor function method
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "constructor" or self.jack_tokenizer.focus_token == "function" or self.jack_tokenizer.focus_token == "method"):
                kind = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(16)
        
        # void type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "void" or self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                type = self.jack_tokenizer.keyWord()
            elif token_type == "IDENTIFIER":
                type = self.jack_tokenizer.identifier()
            else:
                print(17)
        else:
            print(18)
        
        # constructor名はclass名と一致
        if kind == "CONSTRUCTOR":
            if self.class_name != type:
                print("クラス名とコンストラクタ名が異なります")
                return
        # method の場合thisが arg 0 にあたる
        self.is_method = True if kind == "METHOD" else False

        # subroutineName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                name = self.jack_tokenizer.identifier()
            else:
                print(19)
        else:
            print(20)
        
        # (
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                token = self.jack_tokenizer.symbol()
            else:
                print(21)
        else:
            print(22)
        
        # parameterList
        self.compileParameterList()

        # )
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                token = self.jack_tokenizer.symbol()
            else:
                print(23)
        else:
            print(24)
        
        # {
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "{":
                token = self.jack_tokenizer.symbol()
            else:
                print(25)
        else:
            print(26)
        
        # varDec*
        while True:
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "var":
                    self.compileVarDec()
                else:
                    break
            else:
                print(30)
        
        # mvwrite
        # function(subroutine)
        function_name = self.file_name + "." + name
        nLocals = self.symbol_table.varCount("VAR")
        self.vm_writer.writeFunction(function_name, nLocals)

        if kind == "CONSTRUCTOR":
            index = self.symbol_table.varCount("FIELD")
            # field alloc
            segment = "CONST"
            self.vm_writer.writePush(segment, index)
            self.vm_writer.writeCall("Memory.alloc", 1)
            
            # thisにinstanceを設定
            self.vm_writer.writePop("POINTER", 0)
        elif kind == "METHOD":
            self.vm_writer.writePush("ARG", 0)
            self.vm_writer.writePop("POINTER", 0)

        # statements
        self.compileStatements()
        
        # }
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "}":
                token = self.jack_tokenizer.symbol()
            else:
                print(24)
        else:
            return

        return
    

    def compileParameterList(self):
        # type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                type = self.jack_tokenizer.keyWord()
            elif token_type == "IDENTIFIER":
                type = self.jack_tokenizer.identifier()
            else:
                return
        else:
            return
        
        # varName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                name = self.jack_tokenizer.identifier()
            else:
                print(25)
        else:
            print(26)
        
        # arg変数
        self.symbol_table.define(name, type, "ARG")
        
        while True:
            # ,
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ",":
                    token = self.jack_tokenizer.symbol()
                else:
                    # , 以外はbreak
                    break
            else:
                print(27)
            
            # type
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                    type = self.jack_tokenizer.keyWord()
                elif token_type == "IDENTIFIER":
                    type = self.jack_tokenizer.identifier()
                else:
                    print(27.1)
            else:
                print(22.22)

            # varName
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "IDENTIFIER":
                    name = self.jack_tokenizer.identifier()
                else:
                    print(28)
            else:
                print(29)
            
            # local変数
            self.symbol_table.define(name, type, "ARG")
        
        return


    def compileVarDec(self):
        # var (var以外break)
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "var":
                var = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(30)
        
        # type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                type = self.jack_tokenizer.keyWord()
            elif token_type == "IDENTIFIER":
                type = self.jack_tokenizer.identifier()
            else:
                print(31)
        else:
            print(32)
        
        # varName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                name = self.jack_tokenizer.identifier()
            else:
                print(33)
        else:
            print(34)

        # var -> symbol_table.define
        self.symbol_table.define(name, type, "VAR")

        # (, varName)*
        while True:
            # ,
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ",":
                    token = self.jack_tokenizer.symbol()
                else:
                    # , 以外はbreak
                    break
            else:
                print(35)
            
            # varName
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "IDENTIFIER":
                    name = self.jack_tokenizer.identifier()
                else:
                    print(36)
            else:
                print(37)
            
            # var -> symbol_table.define
            self.symbol_table.define(name, type, "VAR")
        
        # ; 
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                token = self.jack_tokenizer.symbol()
            else:
                print(38)
        else:
            print(39)

        return

    
    def compileStatements(self):
        # stetemet*
        while True:
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "KEYWORD":
                    if self.jack_tokenizer.focus_token == "let":
                        self.compileLet()
                    elif self.jack_tokenizer.focus_token == "if" or self.jack_tokenizer.focus_token == "else":
                        self.compileIf()
                    elif self.jack_tokenizer.focus_token == "while":
                        self.compileWhile()
                    elif self.jack_tokenizer.focus_token == "do":
                        self.compileDo()
                    elif self.jack_tokenizer.focus_token == "return":
                        self.compileReturn()
                    else:
                        print(40)
                elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "}":
                    break
                else:
                    print(41)
                    break
            else:
                print(39)
        
        return
    

    def compileLet(self):
        # let
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "let":
                let = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(40)
        
        # varName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                let_var = self.jack_tokenizer.identifier()
            else:
                print(36)
        else:
            print(37)
        
        # [] ?
        # [
        let_array = False
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL":
                if self.jack_tokenizer.focus_token == "[":
                    let_array = True
                    token = self.jack_tokenizer.symbol()

                    # expression
                    self.compileExpression()

                    # ]
                    if self.jack_tokenizer.hasMoreTokens():
                        self.jack_tokenizer.advance()
                        token_type = self.jack_tokenizer.tokenType()
                        if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "]":
                            token = self.jack_tokenizer.symbol()
                        else:
                            print(38)
                    else:
                        print(39)
                    
                    # 配列のベースアドレスをpush
                    #print(name, self.jack_tokenizer.focus_token)
                    segment = self.symbol_table.kindOf(let_var)
                    if segment == "VAR":segment = "LOCAL"
                    if segment == "FIELD": segment = "THIS"
                    index = self.symbol_table.indexOf(let_var) + (segment=="ARG"*self.is_method)
                    self.vm_writer.writePush(segment, index)
                    # ベースアドレス + インデックス
                    self.vm_writer.writeArithmetic("add")
        else:
            print(40)
        
        # =
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "=":
                token = self.jack_tokenizer.symbol()
            else:
                print(41)
        else:
            print(42)
        
        # expression
        self.compileExpression()

        # ;
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                token = self.jack_tokenizer.symbol()
            else:
                print(43)
        else:
            print(44)
        
        # let_varにpop
        if let_array:
            # 代入値を temp 0 へ
            self.vm_writer.writePop("TEMP", 0)
            # ベースアドレス + インデックスを pointer 1 へ
            self.vm_writer.writePop("POINTER", 1)
            # 代入
            self.vm_writer.writePush("TEMP", 0)
            self.vm_writer.writePop("THAT", 0)
        else:
            segment = self.symbol_table.kindOf(let_var)
            if segment == "VAR": segment = "LOCAL"
            if segment == "FIELD":segment = "THIS"
            index = self.symbol_table.indexOf(let_var) + (segment=="ARG"*self.is_method)
            self.vm_writer.writePop(segment, index)
        
        return


    def compileIf(self):
        # if
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "if":
                token = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(45)

        # (
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                token = self.jack_tokenizer.symbol()
            else:
                print(46)
        else:
            print(47)

        # expression
        self.compileExpression()

        # )
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                token = self.jack_tokenizer.symbol()
            else:
                print(48)
        else:
            print(49)

        # if-goto
        true_label = "IF_TRUE" + str(self.if_label)
        false_label = "IF_FALSE" + str(self.if_label)
        end_label = "IF_END" + str(self.if_label)
        self.if_label += 1
        # if-goto true_label
        self.vm_writer.writeIf(true_label)
        # goto false_label
        self.vm_writer.writeGoto(false_label)
        # label true_label
        self.vm_writer.writeLabel(true_label)

        # {
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "{":
                token = self.jack_tokenizer.symbol()
            else:
                print(50)
        else:
            print(51)

        # statements
        self.compileStatements()
        
        # }
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "}":
                token = self.jack_tokenizer.symbol()
            else:
                print(52)
        else:
            print(53)

        # else ?
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "else":
                # false_label
                else_token = self.jack_tokenizer.keyWord()
                self.vm_writer.writeGoto(end_label)
                self.vm_writer.writeLabel(false_label)
            else:
                # end_label
                self.vm_writer.writeLabel(false_label)
                return
        else:
            print(54)

        # {
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "{":
                token = self.jack_tokenizer.symbol()
            else:
                print(55)
        else:
            print(56)

        # statements
        self.compileStatements()

        # }
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "}":
                token = self.jack_tokenizer.symbol()
            else:
                print(57)
        else:
            print(58)
        
        # end_label
        self.vm_writer.writeLabel(end_label)

        return


    def compileWhile(self):
        # while label
        continue_label = "WHILE_EXP" + str(self.while_label)
        end_label = "WHILE_END" + str(self.while_label)
        self.while_label += 1
        self.vm_writer.writeLabel(continue_label)

        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "while":
                while_token = self.jack_tokenizer.keyWord()
            else:
                print(59)
        else:
            print(60)

        # (
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                token = self.jack_tokenizer.symbol()
            else:
                print(61)
        else:
            print(62)

        # expression
        self.compileExpression()

        # )
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                token = self.jack_tokenizer.symbol()
            else:
                print(63)
        else:
            print(64)

        # while end ?
        self.vm_writer.writeArithmetic("not")
        self.vm_writer.writeIf(end_label)

        # {
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "{":
                token = self.jack_tokenizer.symbol()
            else:
                print(65)
        else:
            print(66)

        # statements
        self.compileStatements()

        # }
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "}":
                token = self.jack_tokenizer.symbol()
            else:
                print(67)
        else:
            print(68)
        
        # continue_label
        self.vm_writer.writeGoto(continue_label)
        # end_label
        self.vm_writer.writeLabel(end_label)

        return
        

    def compileDo(self):
        # do
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "do":
                do = self.jack_tokenizer.keyWord()
            else:
                print(69)
        else:
            print(70)

        # subroutineCall
        # 2つめのトークンが.かそれ以外か
        
        # identifier
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                call_function = self.jack_tokenizer.identifier()
            else:
                print(71)
        else:
            print(72)
        
        is_instance = False
        # . ?
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ".":
                # varName is constructor
                if self.symbol_table.kindOf(call_function) is not None:
                    # push instance
                    segment = self.symbol_table.kindOf(call_function)
                    if segment == "VAR":segment = "LOCAL"
                    if segment == "FIELD": segment = "THIS" # 呼び出し先で pointer 0　に this 0 を設定
                    index = self.symbol_table.indexOf(call_function) + (segment=="ARG"*self.is_method)
                    self.vm_writer.writePush(segment, index)
                    call_function = self.symbol_table.typeOf(call_function)
                    is_instance = True
                call_function += self.jack_tokenizer.symbol()

                # . の場合の次 subroutineName
                if self.jack_tokenizer.hasMoreTokens():
                    self.jack_tokenizer.advance()
                    token_type = self.jack_tokenizer.tokenType()
                    if token_type == "IDENTIFIER":
                        call_function += self.jack_tokenizer.identifier()
                    else:
                        print(73)
                else:
                    print(74)
            elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                call_function = self.file_name + "." + call_function
                self.vm_writer.writePush("POINTER", 0)
                is_instance = True
        else:
            print(75)
        
        # (
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                token = self.jack_tokenizer.symbol()
            else:
                print(76)
        else:
            print(77)

        # expressionList
        self.compileExpressionList()

        # )
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                token = self.jack_tokenizer.symbol()
            else:
                print(78)
        else:
            print(79)
        
        # ;
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                token = self.jack_tokenizer.symbol()
            else:
                print(89.1)
        else:
            print(89.2)
        
        # call function, not return
        self.vm_writer.writeCall(call_function, self.nargs+is_instance)
        self.vm_writer.writePop("TEMP", 0)
        return


    def compileReturn(self):
        # return
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "return":
                return_token = self.jack_tokenizer.keyWord()
            else:
                print(80)
        else:
            print(81)
        
        # expression, ; ?
        # ;
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                # return 0
                self.vm_writer.writePush("CONST", 0)
            else:
                self.compileExpression()
        else:
            print(81.2)
        

        # ;
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                token = self.jack_tokenizer.symbol()
            else:
                print(81.1)
        else:
            print(81.2)

        # return
        self.vm_writer.writeReturn()
        return


    def compileExpression(self):
        # op_set
        op_set = set(['+', '-', '*', '/', '&', '|', '<', '>', '='])

        # term
        self.compileTerm()

        while True:
            # op 以外ならbreak
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token in op_set:
                    op = self.jack_tokenizer.symbol()
                else:
                    break
            else:
                print(82)

            # term
            self.compileTerm()

            # op を行う
            if op == "+":
                self.vm_writer.writeArithmetic("add")
            elif op == "-":
                self.vm_writer.writeArithmetic("sub")
            elif op == "*":
                self.vm_writer.writeCall("Math.multiply", 2)
            elif op == "/":
                self.vm_writer.writeCall("Math.divide", 2)
            elif op == "&":
                self.vm_writer.writeArithmetic("and")
            elif op == "|":
                self.vm_writer.writeArithmetic("or")
            elif op == "<":
                self.vm_writer.writeArithmetic("lt")
            elif op == ">":
                self.vm_writer.writeArithmetic("gt")
            elif op == "=":
                self.vm_writer.writeArithmetic("eq")
            else:
                print("op " + op + " が無効")
        
        
        return

    
    def compileTerm(self):
        # unaryOp
        unaryOp_set = set(['-', '~'])

        # KeywordConstant
        keywordConstant_set = set(["true", "false", "null", "this"])
        
        # check type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "INT_CONST":
                num = str(self.jack_tokenizer.intVal())

                # constant int
                self.vm_writer.writePush("CONST", num)
            elif token_type == "STRING_CONST":
                string = self.jack_tokenizer.stringVal()

                # create string
                self.vm_writer.writePush("CONST", len(string))
                self.vm_writer.writeCall("String.new", 1)
                for c in string:
                    self.vm_writer.writePush("CONST", ord(c))
                    self.vm_writer.writeCall("String.appendChar", 2)
            elif token_type == "KEYWORD" and self.jack_tokenizer.focus_token in keywordConstant_set:
                keyword_constant = self.jack_tokenizer.keyWord()
                
                # write keyword_constant
                if keyword_constant == "TRUE":
                    self.vm_writer.writePush("CONST", 0)
                    self.vm_writer.writeArithmetic("not")
                elif keyword_constant == "FALSE":
                    self.vm_writer.writePush("CONST", 0)
                elif keyword_constant == "NULL":
                    self.vm_writer.writePush("CONST", 0)
                elif keyword_constant == "THIS":
                    self.vm_writer.writePush("POINTER", 0)
            elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token in unaryOp_set:
                unaryOp = self.jack_tokenizer.symbol()

                # term
                self.compileTerm()

                if unaryOp == "-":
                    self.vm_writer.writeArithmetic("neg")
                elif unaryOp == "~":
                    self.vm_writer.writeArithmetic("not")

            elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                token = self.jack_tokenizer.symbol()

                self.compileExpression()
                
                # )
                if self.jack_tokenizer.hasMoreTokens():
                    self.jack_tokenizer.advance()
                    token_type = self.jack_tokenizer.tokenType()
                    if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                        token = self.jack_tokenizer.symbol()
                    else:
                        print(83)
                else:
                    print(84)

            # varName
            # varName[expression] | 
            # subroutineName (expressionList) | 
            # (className | varName).subroutineName(expressionList)
            elif token_type == "IDENTIFIER":
                name = self.jack_tokenizer.identifier()
                if self.jack_tokenizer.hasMoreTokens():
                    self.jack_tokenizer.advance()
                    token_type = self.jack_tokenizer.tokenType()

                    # varName[expression]
                    if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "[":
                        token = self.jack_tokenizer.symbol()

                        # expression
                        self.compileExpression()

                        # ]
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "]":
                                token = self.jack_tokenizer.symbol()
                            else:
                                print(85)
                        else:
                            print(86)
                        
                        # 配列のベースアドレスをpush
                        segment = self.symbol_table.kindOf(name)
                        if segment == "VAR":segment = "LOCAL"
                        if segment == "FIELD": segment = "THIS"
                        index = self.symbol_table.indexOf(name) + (segment=="ARG"*self.is_method)
                        self.vm_writer.writePush(segment, index)
                        # ベースアドレス + インデックス
                        self.vm_writer.writeArithmetic("add")
                        # ベースアドレス + インデックス の値をpush
                        self.vm_writer.writePop("POINTER", 1)
                        self.vm_writer.writePush("THAT", 0)

                    # subroutineName (expressionList)
                    elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                        token = self.jack_tokenizer.symbol()

                        # expressionList
                        self.compileExpressionList()

                        # )
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                                token = self.jack_tokenizer.symbol()
                            else:
                                print(87)
                        else:
                            print(88)
                    
                    # (className | varName).subroutineName(expressionList)
                    elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ".":
                        # varName is constructor
                        is_instance = False
                        if self.symbol_table.kindOf(name) is not None:
                            # push instance
                            segment = self.symbol_table.kindOf(name)
                            if segment == "VAR":segment = "LOCAL"
                            if segment == "FIELD": segment = "THIS"
                            index = self.symbol_table.indexOf(name) + (segment=="ARG"*self.is_method)
                            self.vm_writer.writePush(segment, index)
                            name = self.symbol_table.typeOf(name)
                            is_instance = True

                        name += self.jack_tokenizer.symbol()

                        # subroutineName
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "IDENTIFIER":
                                name += self.jack_tokenizer.identifier()
                            else:
                                print(89, self.jack_tokenizer.focus_token, token_type, name)
                        else:
                            print(90)
                        
                        # (
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                                token = self.jack_tokenizer.symbol()
                            else:
                                print(91, self.jack_tokenizer.focus_token)
                        else:
                            print(92)
                        
                        # expressionList
                        self.compileExpressionList()

                        # )
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                                token = self.jack_tokenizer.symbol()
                            else:
                                print(93)
                        else:
                            print(94)
                        
                        self.vm_writer.writeCall(name, self.nargs+is_instance)
                    
                    # varName
                    else:
                        segment = self.symbol_table.kindOf(name)
                        if segment == "VAR":segment = "LOCAL"
                        if segment == "FIELD": segment = "THIS"
                        index = self.symbol_table.indexOf(name) + (segment=="ARG"*self.is_method)
                        self.vm_writer.writePush(segment, index)

                else:
                    print(95)
            else:
                print(96)
        else:
            print(97)
        
        return

    
    def compileExpressionList(self):
        self.nargs = 0
        # expression ?
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                return
            else:
                self.compileExpression()
        else:
            print(99)

        # ) が来たら空
        while True:
            self.nargs += 1
            # , ?
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ",":
                    token = self.jack_tokenizer.symbol()
                else:
                    break
            else:
                print(100)
            
            # expression ?
            self.compileExpression()
        
        return