import sys
import Parser, Code, SymbolTable

# 文字列が数字かどうか判別する関数
def number(symbol):
    for c in symbol:
        if not (48 <= ord(c) <= 57): 
            return False
    return True


# 幅15の2進数を生成する関数
def makeBinary(n):
    binary = ""
    for i in range(15):
        binary = str(n%2) + binary
        n //= 2
    return binary


input_file_name = sys.argv[1]
output_file_name = input_file_name[:-4] + ".hack"

symbol_table = SymbolTable.SymbolTable()

# 1回目 symbol_table構築
parser = Parser.Parser(input_file_name)

address = 0
while parser.hasMoreCommands():
    # コマンド取得
    parser.advance()
    if len(parser.focus_assemble) == 0:continue
    command_type = parser.commandType()
    if command_type == "A_COMMAND" or command_type == "C_COMMAND":
        address += 1
    elif command_type == "L_COMMAND":
        symbol = parser.symbol()
        if symbol not in symbol_table.symbol_table:
            symbol_table.symbol_table[symbol] = address


# 2回目 code生成
parser = Parser.Parser(input_file_name)
code = Code.Code()
output_file = open('{}'.format(output_file_name), "w")
variable_address = 16

while parser.hasMoreCommands():
    # コマンド取得
    parser.advance()

    # 空行は次の行へ
    if len(parser.focus_assemble) == 0:continue
    
    command_type = parser.commandType()
    
    # A_COMMAND (@xxx)
    if command_type == "A_COMMAND":
        symbol = parser.symbol()
        # 変数の場合に symbol_table に入れる それ以外はelse(変数またはシンボル)
        if number(symbol):
            binary_code = "0" + makeBinary(int(symbol))
        else:
            if symbol not in symbol_table.symbol_table:
                symbol_table.symbol_table[symbol] = variable_address
                variable_address += 1
            binary_code = "0" + makeBinary(symbol_table.symbol_table[symbol])
    elif command_type == "C_COMMAND":
        dest_mnemonic = parser.dest()
        comp_mnemonic = parser.comp()
        jump_mnemonic = parser.jump()
        D = code.dest(dest_mnemonic)
        A = "1" if 'M' in comp_mnemonic else "0"
        C = code.comp(comp_mnemonic)
        J = code.jump(jump_mnemonic)
        binary_code = "111" + A + C + D + J
    else:
        continue
    output_file.write(binary_code+"\n")

output_file.close()
