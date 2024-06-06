from typing import List
class SLRTable:
    
    def __init__(self):
        # SLR parsing table 
        # staete number is index and its corresponding value is a dictionary whose keys are valid term(s) and values are actions
        # if 'class' is given at state 0, action 's6' is out
        
        self.table:List[dict] = [
            {"vtype": "s2", "VDECL": "1"},
            {"vtype": "s5", "$": "r2", "CODE": "3", "VDECL": "1", "FDECL": "4"},
            {"id": "s6", "ASSIGN": "7"},
            {"$": "acc"},
            {"vtype": "s5", "$": "r2", "CODE": "8", "VDECL": "1", "FDECL": "4"},
            {"id": "s9", "ASSIGN": "7"},
            {"semi": "s10", "assign": "s11"},
            {"semi": "s12"},
            {"$": "r1"},
            {"semi": "s10", "assign": "s11", "lparen": "s13"},
            {"vtype": "r3", "id": "r3", "rbrace": "r3", "if": "r3", "while": "r3", "return": "r3", "$": "r3"},
            {"id": "s22", "literal": "s16", "character": "s17", "boolstr": "s18", "lparen": "s21", "num": "s23", "RHS": "14", "EXPR": "15", "TERM": "19", "FACTOR": "20"},
            {"vtype": "r4", "id": "r4", "rbrace": "r4", "if": "r4", "while": "r4", "return": "r4", "$": "r4"},
            {"vtype": "s25", "rparen": "r19", "ARG": "24"},
            {"semi": "r5"},
            {"semi": "r6"},
            {"semi": "r7"},
            {"semi": "r8"},
            {"semi": "r9"},
            {"semi": "r11", "addsub": "s26", "rparen": "r11"},
            {"semi": "r13", "addsub": "r13", "multdiv": "s27", "rparen": "r13"},
            {"id": "s22", "lparen": "s21", "num": "s23", "EXPR": "28", "TERM": "19", "FACTOR": "20"},
            {"semi": "r15", "addsub": "r15", "multdiv": "r15", "rparen": "r15"},
            {"semi": "r16", "addsub": "r16", "multdiv": "r16", "rparen": "r16"},
            {"rparen": "s29"},
            {"id": "s30"},
            {"id": "s22", "lparen": "s21", "num": "s23", "EXPR": "31", "TERM": "19", "FACTOR": "20"},
            {"id": "s22", "lparen": "s21", "num": "s23", "TERM": "32", "FACTOR": "20"},
            {"rparen": "s33"},
            {"lbrace": "s34"},
            {"rparen": "r21", "comma": "s36", "MOREARGS": "35"},
            {"semi": "r10", "rparen": "r10"},
            {"semi": "r12", "addsub": "r12", "rparen": "r12"},
            {"semi": "r14", "addsub": "r14", "multdiv": "r14", "rparen": "r14"},
            {"vtype": "s2", "id": "s43", "rbrace": "r23", "if": "s44", "while": "s45", "return": "r23", "VDECL": "39", "ASSIGN": "40", "BLOCK": "37", "STMT": "38", "MATCHED": "41", "UNMATCHED": "42"},
            {"rparen": "r18"},
            {"vtype": "s46"},
            {"return": "s48", "RETURN": "47"},
            {"vtype": "s2", "id": "s43", "rbrace": "r23", "if": "s44", "while": "s45", "return": "r23", "VDECL": "39", "ASSIGN": "40", "BLOCK": "49", "STMT": "38", "MATCHED": "41", "UNMATCHED": "42"},
            {"vtype": "r24", "id": "r24", "rbrace": "r24", "if": "r24", "while": "r24", "return": "r24"},
            {"semi": "s50"},
            {"vtype": "r26", "id": "r26", "rbrace": "r26", "if": "r26", "while": "r26", "return": "r26"},
            {"vtype": "r27", "id": "r27", "rbrace": "r27", "if": "r27", "while": "r27", "return": "r27"},
            {"assign": "s11"},
            {"lparen": "s51"},
            {"lparen": "s52"},
            {"id": "s53"},
            {"rbrace": "s54"},
            {"id": "s22", "literal": "s16", "character": "s17", "boolstr": "s18", "lparen": "s21", "num": "s23", "RHS": "55", "EXPR": "15", "TERM": "19", "FACTOR": "20"},
            {"rbrace": "r22", "return": "r22"},
            {"vtype": "r25", "id": "r25", "rbrace": "r25", "if": "r25", "while": "r25", "return": "r25"},
            {"boolstr": "s58", "COND": "56", "SIMPLECOND": "57"},
            {"boolstr": "s58", "COND": "59", "SIMPLECOND": "57"},
            {"rparen": "r21", "comma": "s36", "MOREARGS": "60"},
            {"vtype": "r17", "$": "r17"},
            {"semi": "s61"},
            {"rparen": "s62", "comp": "s63"},
            {"rparen": "r33", "comp": "r33"},
            {"rparen": "r34", "comp": "r34"},
            {"rparen": "s64", "comp": "s63"},
            {"rparen": "r20"},
            {"rbrace": "r35"},
            {"lbrace": "s65"},
            {"boolstr": "s58", "SIMPLECOND": "66"},
            {"lbrace": "s67"},
            {"vtype": "s2", "id": "s43", "rbrace": "r23", "if": "s44", "while": "s45", "return": "r23", "VDECL": "39", "ASSIGN": "40", "BLOCK": "68", "STMT": "38", "MATCHED": "41", "UNMATCHED": "42"},
            {"rparen": "r32", "comp": "r32"},
            {"vtype": "s2", "id": "s43", "rbrace": "r23", "if": "s44", "while": "s45", "return": "r23", "VDECL": "39", "ASSIGN": "40", "BLOCK": "69", "STMT": "38", "MATCHED": "41", "UNMATCHED": "42"},
            {"rbrace": "s70"},
            {"rbrace": "s71"},
            {"vtype": "r30", "id": "r30", "rbrace": "r30", "if": "r30", "else": "s72", "while": "r30", "return": "r30"},
            {"vtype": "r29", "id": "r29", "rbrace": "r29", "if": "r29", "while": "r29", "return": "r29"},
            {"lbrace": "s73", "if": "s75", "UNMATCHED": "74"},
            {"vtype": "s2", "id": "s43", "rbrace": "r23", "if": "s44", "while": "s45", "return": "r23", "VDECL": "39", "ASSIGN": "40", "BLOCK": "76", "STMT": "38", "MATCHED": "41", "UNMATCHED": "42"},
            {"vtype": "r31", "id": "r31", "rbrace": "r31", "if": "r31", "while": "r31", "return": "r31"},
            {"lparen": "s77"},
            {"rbrace": "s78"},
            {"boolstr": "s58", "COND": "79", "SIMPLECOND": "57"},
            {"vtype": "r28", "id": "r28", "rbrace": "r28", "if": "r28", "while": "r28", "return": "r28"},
            {"rparen": "s80", "comp": "s63"},
            {"lbrace": "s81"},
            {"vtype": "s2", "id": "s43", "rbrace": "r23", "if": "s44", "while": "s45", "return": "r23", "VDECL": "39", "ASSIGN": "40", "BLOCK": "82", "STMT": "38", "MATCHED": "41", "UNMATCHED": "42"},
            {"rbrace": "s83"},
            {"vtype": "r30", "id": "r30", "rbrace": "r30", "if": "r30", "else": "s84", "while": "r30", "return": "r30"},
            {"if": "s75", "UNMATCHED": "74"}]
        self.terminal: List[str] = ['vtype', 'num', 'character', 'boolstr', 'literal', 'id', 'if', 'else', 'while', 'return', 'addsub', 'multdiv', 'assign', 'comp', 'semi', 'comma', 'lparen', 'rparen', 'lbrace', 'rbrace']
    
    
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