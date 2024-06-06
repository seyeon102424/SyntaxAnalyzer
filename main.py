from SLRTable import SLRTable
from SyntaxAnalyzer import SyntaxAnalyzer
from typing import List
from Node import Node
import sys



slr_table: SLRTable = SLRTable()
syntax_analyzer:SyntaxAnalyzer = SyntaxAnalyzer(slr_table)

if len(sys.argv) < 2:
    print("write your file path")
    sys.exit(1)

file_path:str= str(sys.argv[1])

parse_tree_list = []

with open(file_path, 'r') as token_sequence_file:
    for line_number, line in enumerate(token_sequence_file):
        if line[-1] == '\n':
            line = line[:-1]
        parse_Node:Node = syntax_analyzer.verify(line)
       
        if parse_Node == None:
            print("at line " + str(line_number + 1))
        else:
            parse_tree_list.append(parse_Node.get_parse_tree_string())
                
            print()
            parse_Node.draw_Node()
                
with open("../output/output.txt", 'w') as output_file:
    for line in parse_tree_list:
        output_file.write(line + "\n")




# classify accept and reject of token sequences from an input file
"""
def test_and_classify_file(file_path):
    accepted_result_file_path:str = file_path.split(".")[0] + "_accepted" + ".txt"
    rejected_result_file_path:str = file_path.split(".")[0] + "_rejected" + ".txt"


    accepted_test_lines:List[str] = []
    rejected_test_lines:List[str] = []
    with open(file_path, 'r') as test_file:
        for line in test_file:
            parse_Node:Node = syntax_analyzer.verify(line)

            if parse_Node != None:
                accepted_test_lines.append(line)
            else:
                rejected_test_lines.append(line)

    
    accepted_test_lines = set(accepted_test_lines)
    rejected_test_lines = set(rejected_test_lines)

    with open(accepted_result_file_path, 'w') as accepted_test_file:
        for line in accepted_test_lines:
            accepted_test_file.write(line)

    with open(rejected_result_file_path, 'w') as rejected_test_file:
        for line in rejected_test_lines:
            rejected_test_file.write(line)


file_path:str= str(sys.argv[1])
test_and_classify_file(file_path)
"""











# draw parse Nodes for token sequences randomly chosen from the accepted ones
"""
# draw a parse Node, given a token sequence
def draw_parse_Node(token_sequence: str)-> None: 
    parse_Node:Node = syntax_analyzer.verify(token_sequence)

    if parse_Node == None:
        print("can't draw a parse Node")
    else:
        print()
        parse_Node.draw_Node()

print("-----------test for parse Nodes-----------")
draw_parse_Node("class id lbrace vtype id assign boolstr semi vtype id lparen vtype id comma vtype id rparen lbrace return literal semi rbrace vtype id semi vtype id semi rbrace class id lbrace rbrace")
print("--------------------------------------------")
draw_parse_Node("vtype id semi vtype id semi vtype id lparen vtype id comma vtype id rparen lbrace vtype id semi while lparen boolstr rparen lbrace rbrace return boolstr semi rbrace vtype id lparen rparen lbrace while lparen boolstr rparen lbrace rbrace return character semi rbrace vtype id assign literal semi class id lbrace rbrace vtype id semi")
print("--------------------------------------------")
draw_parse_Node("vtype id lparen rparen lbrace id assign literal semi id assign boolstr semi return num semi rbrace vtype id semi")
print("--------------------------------------------")
draw_parse_Node("class id lbrace rbrace class id lbrace vtype id assign literal semi rbrace vtype id lparen vtype id rparen lbrace return literal semi rbrace")
"""





# test for rejected token sequences randomly chosen from the rejected ones
"""
print("-----------test for rejection-----------")
syntax_analyzer.verify("class id lbrace vtype id assign id addsub multdiv semi vtype id assign character semi rbrace vtype id semi")
print("--------------------------------------------")
syntax_analyzer.verify("class id lbrace rbrace class id lbrace rbrace vtype id lparen vtype id rparen lbrace return boolstr semi rbrace vtype id lparen rparen lbrace while lparen boolstr rparen lbrace if lparen rparen lbrace rbrace rbrace return semi rbrace vtype id lparen vtype id comma vtype id comma vtype id rparen lbrace while lparen boolstr rparen lbrace rbrace return addsub semi rbrace vtype id lparen vtype id comma vtype id rparen lbrace return literal semi rbrace vtype id lparen rparen lbrace return semi rbrace class id lbrace rbrace")
print("--------------------------------------------")
syntax_analyzer.verify("vtype id semi vtype id assign character semi vtype id assign literal semi vtype id lparen vtype id comma vtype id comma vtype id rparen lbrace vtype id semi while lparen rparen lbrace rbrace return semi rbrace")
print("--------------------------------------------")
syntax_analyzer.verify("vtype id lparen rparen lbrace return num multdiv num multdiv multdiv addsub id addsub multdiv semi rbrace class id lbrace rbrace vtype id assign multdiv addsub addsub semi")
print()
"""





# test for the empty string
"""
print("-----------test for the empty string-----------")
syntax_analyzer.verify("")
"""







# test for a token sequence that conntains any undefined terminal
# undefined terminals are pushed as an input sequence such as clas, brace, type
"""
print("-----------test for undefined terminal-----------")
syntax_analyzer.verify("clas id brace type id assign id addsub multdiv semi vtype id assign character semi rbrace vtype id semi")
"""