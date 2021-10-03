import CodeWriter, Parser
import sys
import glob

if sys.argv[1][-3] == ".":
    file_name = sys.argv[1][:-3] + ".asm"
    input_files = [sys.argv[1]]
else:
    directory_name = sys.argv[1]
    file_name = ""
    for c in directory_name[::-1]:
        if c == "/":break
        file_name = c + file_name
    file_name = directory_name + "/" + file_name + ".asm"
    input_files = glob.glob("./"+sys.argv[1]+"/*.vm")

codeWriter = CodeWriter.CodeWriter("./"+ file_name)
if len(input_files) > 1:codeWriter.writeInit()

try:
    for file in input_files:
        parser = Parser.Parser(file)
        codeWriter.setFileName(file[:-3])

        while parser.hasMoreCommands():
            parser.advance()
            if len(parser.args) == 0: continue

            command_type = parser.commandType()
            if command_type == "C_ARITHMETIC":
                command = parser.arg1()
                codeWriter.writeArithmetic(command)
            elif command_type == "C_PUSH" or command_type == "C_POP":
                command = parser.arg1()
                segment = parser.arg2()
                index = parser.arg3()
                codeWriter.writePushPop(command, segment, index)
            elif command_type == "C_LABEL":
                label = parser.arg2()
                codeWriter.writeLabel(label)
            elif command_type == "C_GOTO":
                label = parser.arg2()
                codeWriter.writeGoto(label)
            elif command_type == "C_IF":
                label = parser.arg2()
                codeWriter.writeIf(label)
            elif command_type == "C_CALL":
                functionName = parser.arg2()
                numArgs = parser.arg3()
                codeWriter.writeCall(functionName, numArgs)
            elif command_type == "C_RETURN":
                codeWriter.writeReturn()
            elif command_type == "C_FUNCTION":
                functionName = parser.arg2()
                numLocals = parser.arg3()
                codeWriter.writeFunction(functionName, numLocals)

finally:
    codeWriter.close()