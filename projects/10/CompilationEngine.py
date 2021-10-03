class CompilationEngine:
    import JackTokenizer
    import xml.etree.ElementTree as ET
    def __init__(self, input_file, output_file):
        self.jack_tokenizer = self.JackTokenizer.JackTokenizer(input_file)
        self.output_file = open(output_file, mode="wb")
        self.xml_nest = list()
        print()
        print(output_file)
        print()
        # dfs start
        self.compileClass()

    

    def compileClass(self):
        # <class> 生成
        self.xml_nest.append(self.ET.Element("class"))

        # class
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "class":
                class_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                class_xml.text = self.jack_tokenizer.keyWord()
            else:
                print(1)
        else:
            return
        
        # class名
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                identifier_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                identifier_xml.text = self.jack_tokenizer.identifier()
            else:
                print(3)
        else:
            return

        # <symbol> { </symbol>
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL":
                identifier_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                identifier_xml.text = self.jack_tokenizer.symbol()
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
                    print()
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
                identifier_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                identifier_xml.text = self.jack_tokenizer.symbol()
            else:
                print(5)
        else:
            return
        
        # ファイルに書き込み、ファイルを閉じる
        tree = self.ET.ElementTree(self.xml_nest[0])
        tree.write(self.output_file)
        self.output_file.close()
    


    def compileClassVarDec(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "classVarDec"))

        # static field
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "static" or self.jack_tokenizer.focus_token == "field"):
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(6)
        
        # type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            elif token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(7)
        else:
            print(8)
        
        # varName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(9)
        else:
            print(10)
        
        # (, varName)*
        while True:
            # ,
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ",":
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                    keyword_xml.text = self.jack_tokenizer.symbol()
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
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                    keyword_xml.text = self.jack_tokenizer.identifier()
                else:
                    print(12)
            else:
                print(13)
        
        # ; 
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(14)
        else:
            print(15)
        
        self.xml_nest.pop()
        return
    

    def compileSubroutine(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "subroutineDec"))

        # constructor function method
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "constructor" or self.jack_tokenizer.focus_token == "function" or self.jack_tokenizer.focus_token == "method"):
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(16)
        
        # void type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "void" or self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            elif token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(17)
        else:
            print(18)
        
        # subroutineName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(19)
        else:
            print(20)
        
        # (
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                identifier_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                identifier_xml.text = self.jack_tokenizer.symbol()
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
                identifier_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                identifier_xml.text = self.jack_tokenizer.symbol()
            else:
                print(23)
        else:
            print(24)
        
        # subroutineBody
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "subroutineBody"))
        # {
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "{":
                identifier_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                identifier_xml.text = self.jack_tokenizer.symbol()
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

        # statements
        self.compileStatements()
        
        # }
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "}":
                identifier_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                identifier_xml.text = self.jack_tokenizer.symbol()
            else:
                print(24)
        else:
            return
        
        self.xml_nest.pop()
        
        self.xml_nest.pop()
        print(self.xml_nest)
        return
    

    def compileParameterList(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "parameterList"))

        # type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            elif token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                self.xml_nest.pop()
                return
        else:
            return
        
        # varName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(25)
        else:
            print(26)
        
        while True:
            # ,
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ",":
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                    keyword_xml.text = self.jack_tokenizer.symbol()
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
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                    keyword_xml.text = self.jack_tokenizer.keyWord()
                elif token_type == "IDENTIFIER":
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                    keyword_xml.text = self.jack_tokenizer.identifier()
                else:
                    print(27.1)
            else:
                print(22.22)

            # varName
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "IDENTIFIER":
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                    keyword_xml.text = self.jack_tokenizer.identifier()
                else:
                    print(28)
            else:
                print(29)
        
        self.xml_nest.pop()
        return


    def compileVarDec(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "varDec"))

        # var (var以外break)
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "var":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(30)
        
        # type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and (self.jack_tokenizer.focus_token == "int" or self.jack_tokenizer.focus_token == "char" or self.jack_tokenizer.focus_token == "boolean"):
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            elif token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(31)
        else:
            print(32)
        
        # varName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(33)
        else:
            print(34)

        # (, varName)*
        while True:
            # ,
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ",":
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                    keyword_xml.text = self.jack_tokenizer.symbol()
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
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                    keyword_xml.text = self.jack_tokenizer.identifier()
                else:
                    print(36)
            else:
                print(37)
        
        # ; 
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(38)
        else:
            print(39)

        self.xml_nest.pop()
        return

    
    def compileStatements(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "statements"))

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
        
        self.xml_nest.pop()
        return
    

    def compileLet(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "letStatement"))

        # let
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "let":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(40)
        
        # varName
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(36)
        else:
            print(37)
        
        # [] ?
        # [
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL":
                if self.jack_tokenizer.focus_token == "[":
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                    keyword_xml.text = self.jack_tokenizer.symbol()

                    # expression
                    self.compileExpression()

                    # ]
                    if self.jack_tokenizer.hasMoreTokens():
                        self.jack_tokenizer.advance()
                        token_type = self.jack_tokenizer.tokenType()
                        if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "]":
                            keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                            keyword_xml.text = self.jack_tokenizer.symbol()
                        else:
                            print(38)
                    else:
                        print(39)
        else:
            print(40)
        
        # =
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "=":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(43)
        else:
            print(44)
        
        self.xml_nest.pop()
        return


    def compileIf(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "ifStatement"))

        # if
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "if":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            else:
                return
        else:
            print(45)

        # (
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(48)
        else:
            print(49)

        # {
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "{":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(52)
        else:
            print(53)

        # else ?
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "else":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            else:
                self.xml_nest.pop()
                return
        else:
            print(54)

        # {
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "{":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(57)
        else:
            print(58)
        
        self.xml_nest.pop()
        return


    def compileWhile(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "whileStatement"))

        # while
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "while":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            else:
                print(59)
        else:
            print(60)

        # (
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(63)
        else:
            print(64)
        
        # {
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "{":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(67)
        else:
            print(68)
        
        self.xml_nest.pop()
        return
        

    def compileDo(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "doStatement"))

        # do
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "do":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()
            else:
                print(71)
        else:
            print(72)
        
        # . ?
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ".":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()

                # . の場合の次 subroutineName
                if self.jack_tokenizer.hasMoreTokens():
                    self.jack_tokenizer.advance()
                    token_type = self.jack_tokenizer.tokenType()
                    if token_type == "IDENTIFIER":
                        keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                        keyword_xml.text = self.jack_tokenizer.identifier()
                    else:
                        print(73)
                else:
                    print(74)
        else:
            print(75)
        
        # (
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(78)
        else:
            print(79)
        
        # ;
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(89.1)
        else:
            print(89.2)
        
        self.xml_nest.pop()
        return


    def compileReturn(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "returnStatement"))

        # return
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "KEYWORD" and self.jack_tokenizer.focus_token == "return":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
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
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()

                self.xml_nest.pop()
                return
            else:
                self.compileExpression()
        else:
            print(81.2)
        

        # ;
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ";":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()
            else:
                print(81.1)
        else:
            print(81.2)

        self.xml_nest.pop()
        return


    def compileExpression(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "expression"))

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
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                    keyword_xml.text = self.jack_tokenizer.symbol()
                else:
                    break
            else:
                print(82)

            # term
            self.compileTerm()
        
        self.xml_nest.pop()
        return

    
    def compileTerm(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "term"))

        # unaryOp
        unaryOp_set = set(['-', '~'])

        # KeywordConstant
        keywordConstant_set = set(["true", "false", "null", "this"])

        # check type
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "INT_CONST":
                int_xml = self.ET.SubElement(self.xml_nest[-1], "integerConstant")
                int_xml.text = str(self.jack_tokenizer.intVal())
            
            elif token_type == "STRING_CONST":
                int_xml = self.ET.SubElement(self.xml_nest[-1], "stringConstant")
                int_xml.text = self.jack_tokenizer.stringVal()
            
            elif token_type == "KEYWORD" and self.jack_tokenizer.focus_token in keywordConstant_set:
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "keyword")
                keyword_xml.text = self.jack_tokenizer.keyWord()
            
            elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token in unaryOp_set:
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()

                # term
                self.compileTerm()

            elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                keyword_xml.text = self.jack_tokenizer.symbol()

                self.compileExpression()
                
                # )
                if self.jack_tokenizer.hasMoreTokens():
                    self.jack_tokenizer.advance()
                    token_type = self.jack_tokenizer.tokenType()
                    if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                        keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                        keyword_xml.text = self.jack_tokenizer.symbol()
                    else:
                        print(83)
                else:
                    print(84)

            # varName
            # varName[expression] | 
            # subroutineName (expressionList) | 
            # (className | varName).subroutineName(expressionList)
            elif token_type == "IDENTIFIER":
                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                keyword_xml.text = self.jack_tokenizer.identifier()

                if self.jack_tokenizer.hasMoreTokens():
                    self.jack_tokenizer.advance()
                    token_type = self.jack_tokenizer.tokenType()

                    # varName[expression]
                    if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "[":
                        keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                        keyword_xml.text = self.jack_tokenizer.symbol()

                        # expression
                        self.compileExpression()

                        # ]
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "]":
                                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                                keyword_xml.text = self.jack_tokenizer.symbol()
                            else:
                                print(85)
                        else:
                            print(86)

                    # subroutineName (expressionList)
                    elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                        keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                        keyword_xml.text = self.jack_tokenizer.symbol()

                        # expressionList
                        self.compileExpressionList()

                        # )
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                                keyword_xml.text = self.jack_tokenizer.symbol()
                            else:
                                print(87)
                        else:
                            print(88)
                    
                    # (className | varName).subroutineName(expressionList)
                    elif token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ".":
                        keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                        keyword_xml.text = self.jack_tokenizer.symbol()

                        # subroutineName
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "IDENTIFIER":
                                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "identifier")
                                keyword_xml.text = self.jack_tokenizer.identifier()
                            else:
                                print(89)
                        else:
                            print(90)
                        
                        # (
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == "(":
                                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                                keyword_xml.text = self.jack_tokenizer.symbol()
                            else:
                                print(91)
                        else:
                            print(92)
                        
                        # expressionList
                        self.compileExpressionList()

                        # )
                        if self.jack_tokenizer.hasMoreTokens():
                            self.jack_tokenizer.advance()
                            token_type = self.jack_tokenizer.tokenType()
                            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                                keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                                keyword_xml.text = self.jack_tokenizer.symbol()
                            else:
                                print(93)
                        else:
                            print(94)
                    
                    # varName
                    else:
                        pass

                else:
                    print(95)
            else:
                print(96)
        else:
            print(97)
        
        self.xml_nest.pop()
        return

    
    def compileExpressionList(self):
        self.xml_nest.append(self.ET.SubElement(self.xml_nest[-1], "expressionList"))

        # expression ?
        if self.jack_tokenizer.hasMoreTokens():
            self.jack_tokenizer.advance()
            token_type = self.jack_tokenizer.tokenType()
            if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ")":
                self.xml_nest.pop()
                return
            else:
                self.compileExpression()
        else:
            print(99)

        # ) が来たら空
        while True:
            # , ?
            if self.jack_tokenizer.hasMoreTokens():
                self.jack_tokenizer.advance()
                token_type = self.jack_tokenizer.tokenType()
                if token_type == "SYMBOL" and self.jack_tokenizer.focus_token == ",":
                    keyword_xml = self.ET.SubElement(self.xml_nest[-1], "symbol")
                    keyword_xml.text = self.jack_tokenizer.symbol()
                else:
                    break
            else:
                print(100)
            
            # expression ?
            self.compileExpression()
        
        self.xml_nest.pop()
        return