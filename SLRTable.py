from typing import List
class SLRTable:
    
    def __init__(self):
        # SLR parsing table 
        # staete number is index and its corresponding value is a dictionary whose keys are valid term(s) and values are actions
        # if 'class' is given at state 0, action 's6' is out
        
        self.table:List[dict] = [{'vtype': 's5', 'class': 's6', '$': 'r4', 'CODE': '1', 'VDECL': '2', 'FDECL': '3', 'CDECL': '4'}, {'$': 'acc'}, {'vtype': 's5', 'class': 's6', '$': 'r4', 'CODE': '7', 'VDECL': '2', 'FDECL': '3', 'CDECL': '4'}, {'vtype': 's5', 'class': 's6', '$': 'r4', 'CODE': '8', 'VDECL': '2', 'FDECL': '3', 'CDECL': '4'}, {'vtype': 's5', 'class': 's6', '$': 'r4', 'CODE': '9', 'VDECL': '2', 'FDECL': '3', 'CDECL': '4'}, {'id': 's10', 'ASSIGN': '11'}, {'id': 's12'}, {'$': 'r1'}, {'$': 'r2'}, {'$': 'r3'}, {'semi': 's13', 'assign': 's15', 'lparen': 's14'}, {'semi': 's16'}, {'lbrace': 's17'}, {'vtype': 'r5', 'id': 'r5', 'rbrace': 'r5', 'if': 'r5', 'while': 'r5', 'return': 'r5', 'class': 'r5', '$': 'r5'}, {'vtype': 's19', 'rparen': 'r21', 'ARG': '18'}, {'id': 's29', 'character': 's22', 'literal': 's23', 'boolstr': 's24', 'num': 's27', 'lparen': 's28', 'RHS': '20', 'EXPR': '21', 'TERM': '25', 'FACT': '26'}, {'vtype': 'r6', 'id': 'r6', 'rbrace': 'r6', 'if': 'r6', 'while': 'r6', 'return': 'r6', 'class': 'r6', '$': 'r6'}, {'vtype': 's5', 'rbrace': 'r39', 'VDECL': '31', 'FDECL': '32', 'ODECL': '30'}, {'rparen': 's33'}, {'id': 's34'}, {'semi': 'r7'}, {'semi': 'r8'}, {'semi': 'r9'}, {'semi': 'r10'}, {'semi': 'r11'}, {'semi': 'r13', 'addsub': 's35', 'rparen': 'r13'}, {'semi': 'r15', 'addsub': 'r15', 'multdiv': 's36', 'rparen': 'r15'}, {'semi': 'r16', 'addsub': 'r16', 'multdiv': 'r16', 'rparen': 'r16'}, {'id': 's29', 'num': 's27', 'lparen': 's28', 'EXPR': '37', 'TERM': '25', 'FACT': '26'}, {'semi': 'r18', 'addsub': 'r18', 'multdiv': 'r18', 'rparen': 'r18'}, {'rbrace': 's38'}, {'vtype': 's5', 'rbrace': 'r39', 'VDECL': '31', 'FDECL': '32', 'ODECL': '39'}, {'vtype': 's5', 'rbrace': 'r39', 'VDECL': '31', 'FDECL': '32', 'ODECL': '40'}, {'lbrace': 's41'}, {'rparen': 'r23', 'comma': 's43', 'MOREARGS': '42'}, {'id': 's29', 'num': 's27', 'lparen': 's28', 'EXPR': '44', 'TERM': '25', 'FACT': '26'}, {'id': 's29', 'num': 's27', 'lparen': 's28', 'TERM': '45', 'FACT': '26'}, {'rparen': 's46'}, {'vtype': 'r36', 'class': 'r36', '$': 'r36'}, {'rbrace': 'r37'}, {'rbrace': 'r38'}, {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': '49', 'ASSIGN': '50', 'BLOCK': '47', 'STMT': '48'}, {'rparen': 'r20'}, {'vtype': 's55'}, {'semi': 'r12', 'rparen': 'r12'}, {'semi': 'r14', 'addsub': 'r14', 'rparen': 'r14'}, {'semi': 'r17', 'addsub': 'r17', 'multdiv': 'r17', 'rparen': 'r17'}, {'return': 's57', 'RETURN': '56'}, {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': '49', 'ASSIGN': '50', 'BLOCK': '58', 'STMT': '48'}, {'vtype': 'r26', 'id': 'r26', 'rbrace': 'r26', 'if': 'r26', 'while': 'r26', 'return': 'r26'}, {'semi': 's59'}, {'lparen': 's60'}, {'lparen': 's61'}, {'id': 's62', 'ASSIGN': '11'}, {'assign': 's15'}, {'id': 's63'}, {'rbrace': 's64'}, {'id': 's29', 'character': 's22', 'literal': 's23', 'boolstr': 's24', 'num': 's27', 'lparen': 's28', 'RHS': '65', 'EXPR': '21', 'TERM': '25', 'FACT': '26'}, {'rbrace': 'r24', 'return': 'r24'}, {'vtype': 'r27', 'id': 'r27', 'rbrace': 'r27', 'if': 'r27', 'while': 'r27', 'return': 'r27'}, {'boolstr': 's67', 'COND': '66'}, {'boolstr': 's67', 'COND': '68'}, {'semi': 's13', 'assign': 's15'}, {'rparen': 'r23', 'comma': 's43', 'MOREARGS': '69'}, {'vtype': 'r19', 'rbrace': 'r19', 'class': 'r19', '$': 'r19'}, {'semi': 's70'}, {'rparen': 's71'}, {'rparen': 'r32', 'comp': 's73', 'COND_EXPR': '72'}, {'rparen': 's74'}, {'rparen': 'r22'}, {'rbrace': 'r35'}, {'lbrace': 's75'}, {'rparen': 'r30'}, {'boolstr': 's67', 'COND': '76'}, {'lbrace': 's77'}, {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': '49', 'ASSIGN': '50', 'BLOCK': '78', 'STMT': '48'}, {'rparen': 'r31'}, {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': '49', 'ASSIGN': '50', 'BLOCK': '79', 'STMT': '48'}, {'rbrace': 's80'}, {'rbrace': 's81'}, {'vtype': 'r34', 'id': 'r34', 'rbrace': 'r34', 'if': 'r34', 'while': 'r34', 'else': 's83', 'return': 'r34', 'ELSE': '82'}, {'vtype': 'r29', 'id': 'r29', 'rbrace': 'r29', 'if': 'r29', 'while': 'r29', 'return': 'r29'}, {'vtype': 'r28', 'id': 'r28', 'rbrace': 'r28', 'if': 'r28', 'while': 'r28', 'return': 'r28'}, {'lbrace': 's84'}, {'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25', 'VDECL': '49', 'ASSIGN': '50', 'BLOCK': '85', 'STMT': '48'}, {'rbrace': 's86'}, {'vtype': 'r33', 'id': 'r33', 'rbrace': 'r33', 'if': 'r33', 'while': 'r33', 'return': 'r33'}]
        self.terminal: List[str] = ['rbrace', 'comma', 'semi', 'class', 'while', 'multdiv', 'boolstr', 'literal', 'if', 'id', 'assign', 'character', 'lbrace', 'lparen', 'rparen', 'vtype', 'else', 'num', 'addsub', 'return', 'comp']
    
    
    def get_action(self, current_state: int, input_token: str)-> str:
        
        return self.table[current_state][input_token]
    

    # return expected tokens, in case of error
    # for example, state 1 only matches with '$'. So if another term comes in, it raises a key error
    # in that case, the keys of index 1's dicionary of table is returend as a comma-separated string
    def get_expected_token_list(self, current_state: int)-> str:
        expected_symbol_list:List[str] = self.table[current_state].keys()
        expected_token_list:List[str] = []
        for symbol in expected_symbol_list:
            if symbol in self.terminal:
                expected_token_list.append(symbol)
        
        return ", ".join(expected_token_list)
    
    def get_terminal_list(self)-> List[str]:
        return self.terminal
    


    # table = [
    #     {'vtype': 's1', 'VDECL': '2'},
    #     {'id': 's3'},
    #     {'semi': 'r2', 'VDECL': '4', 'CODE': '3'},
    #     {'id':'s2', 'CODE': '1'},
    #     {'semi': 's1', 'VDECL': '0'}
    # ]