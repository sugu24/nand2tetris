from CompilationEngine import CompilationEngine
import sys
import glob
import CompilationEngine

if sys.argv[1][-4:] == ".jack":
    input_files = [sys.argv[1]]
else:
    input_files = glob.glob("./"+sys.argv[1]+"/*.jack")


for input_file in input_files:
    # compilation_engine を生成
    output_file = input_file[:-4] + "1.xml" 
    compilation_engine = CompilationEngine.CompilationEngine(input_file, output_file)

