from typing import List
from collections import deque
import SLRTable
from Node import Node

# action and goto are treated as 'action' in the context
# 'term' means a non-terminal or terminal



class SyntaxAnalyzer:
    def __init__(self, table: SLRTable):
        # stack that saves states
        self.stack: deque[int] = deque()
        # left substring is a deque of Node, in that the proess of push and pop of left substring works the same way to that of creating a parse Node
        self.left_substring: deque[Node] = deque()
        self.right_substring: deque[str] = deque()
        self.table: SLRTable = table

        # Define CFG. 
        # ith production rule occupies ith index. -> 0th production rule is mapped onto index 0
        # Each element looks like [[RHS, LHS], [RHS, LHS], [RHS, LHS] ...]
        self.cfg: List[List[str]] = [['CODE', 'S'],
        ['VDECL CODE', 'CODE'],
        ['FDECL CODE', 'CODE'],
        ['CDECL CODE', 'CODE'],
        ['', 'CODE'],
        ['vtype id semi', 'VDECL'],
        ['vtype ASSIGN semi', 'VDECL'],
        ['id assign RHS', 'ASSIGN'],
        ['EXPR', 'RHS'],
        ['character', 'RHS'],
        ['literal', 'RHS'],
        ['boolstr', 'RHS'],
        ['TERM addsub EXPR', 'EXPR'],
        ['TERM', 'EXPR'],
        ['FACT multdiv TERM', 'TERM'],
        ['FACT', 'TERM'],
        ['num', 'FACT'],
        ['lparen EXPR rparen', 'FACT'],
        ['id', 'FACT'],
        ['vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace', 'FDECL'],
        ['vtype id MOREARGS', 'ARG'],
        ['', 'ARG'],
        ['comma vtype id MOREARGS', 'MOREARGS'],
        ['', 'MOREARGS'],
        ['STMT BLOCK', 'BLOCK'],
        ['', 'BLOCK'],
        ['VDECL', 'STMT'],
        ['ASSIGN semi', 'STMT'],
        ['if lparen COND rparen lbrace BLOCK rbrace ELSE', 'STMT'],
        ['while lparen COND rparen lbrace BLOCK rbrace', 'STMT'],
        ['boolstr COND_EXPR', 'COND'],
        ['comp COND', 'COND_EXPR'],
        ['', 'COND_EXPR'],
        ['else lbrace BLOCK rbrace', 'ELSE'],
        ['', 'ELSE'],
        ['return RHS semi', 'RETURN'],
        ['class id lbrace ODECL rbrace', 'CDECL'],
        ['VDECL ODECL', 'ODECL'],
        ['FDECL ODECL', 'ODECL'],
        ['', 'ODECL']]
       

    def verify(self, token_sequence: str) -> Node:
        # If token sequence is empty
        if not token_sequence:
            print("The token sequence is empty")
            return None
        
        # If any invalid token is contained
        if self.is_invalid_token_sequence(token_sequence.split()):
            return None
        
        # Initial set-up for right substring and stack. 
        self.right_substring = deque(token_sequence.split() + ["$"])

        # The start state is 0
        self.stack.append(0)
        

        
        # Check the token sequence until encountering accept or reject
        while True:
            # get the current state from the top of stack
            current_state = self.stack[-1]

            # prediction is implemented by looking at the first terminal of right substring
            next_symbol = self.right_substring[0]
	
            try:
                # get the appropriate action based on current state and next symbol
                
                action = self.table.get_action(current_state, next_symbol)

                # implement the action. 'implement_action' method returns True, if it encounters 'acc', which means the input sequence is accepted.
                is_accepted = self.implement_action(action)
            
            # key error implies that there is no action for the current_state and next symbol, which means rejection!
            # the reason why key error implies no action refers to SRLTable
            except KeyError:

                print("After " + self.left_substring[-1].get_token() + ", expected token(s): " + self.table.get_expected_token_list(current_state) + ", but the input token: " + next_symbol, end = " ")
                return None


            # if is_accepted is true, return the parse Node
            if is_accepted:
                return self.left_substring[0]
            

    def implement_action(self, action: str)-> bool:
        # four action types
        """
        consisting only of numbers -> goto
        string that start with s -> shift
        string that start with r -> reduce
        string that is acc -> accept
        """

        # if action string(the input) consists only of digits, the action is goto.
        if not action.isdigit():
            # if the action stirng starts with s, shift and update the current state with the number after s
            if action[0] == 's':
                self.shift()
                self.goto(int(action[1:]))
                return False
            # if the action stirng starts with r, reduce with the number after r
            elif action[0] == 'r':
                self.reduce(int(action[1:]))
                return False

            elif action == 'acc':
                return True
        
        # all digits mean goto. just append state
        else:  # GOTO
            self.goto(int(action))
            return False

    # shift is implemented by popping the left most termianl of right substring and appending it to left substring

    def goto(self, next_state:int):
        self.stack.append(next_state)

    def shift(self) -> None:
        new_token_Node: Node = Node(self.right_substring.popleft())
        self.left_substring.append(new_token_Node)


    
    def reduce(self, rule_number: int) -> None:
        # get production rule from CFG by the input index(rule_number)
        production_rule = self.cfg[rule_number]
        # separate the rule into LHS and RHS. RHS consits of multiple terms delimited by a white spae. so split it.
        LHS = production_rule[1]
        RHS = deque(production_rule[0].split())

        # the root for new Node on the production
        # for example, if the prodiction rule is VDECL → vtype id semi, the root is VDECL
        new_token_root: Node = Node(LHS)


        # if RHS is not empty(not epsilon move)
        if RHS:

            # if RHS is vtype id semi, the matching suffix is 'semi id vtype', so reverse RHS and loop to cheeck each  token is well matched
            for token in reversed(RHS):
                reduced_token = self.left_substring.pop()
                if token == reduced_token.get_token():

                    # add chiled to the created root. ex) VDECL is the root and vtype, id, and semi hang onto VDECL
                    new_token_root.add_child(reduced_token)
                    # pop states as many times as the number of RHS
                    self.stack.pop()

        # append the new root to left substring
        self.left_substring.append(new_token_root)

        # do action recursively
        action = self.table.get_action(self.stack[-1], LHS)
        self.implement_action(action)

    

    def is_invalid_token_sequence(self, token_sequence: List[str]) -> bool:
        res = False
        invalid_token_list = []
        for token in token_sequence:
            if token not in self.table.get_terminal_list():
                invalid_token_list.append(token)
                res = True
        
        if res:
            print("INVALID token(s): " + ", ".join(invalid_token_list), end=" ")

        return res
        



    # for test
    """
    def print_status(self):
        left_substring_list:List[str] = []
        for x in self.left_substring:
            left_substring_list.append(x.get_token())
        print(list(self.stack))
        print(left_substring_list)
        print(list(self.right_substring))
    """