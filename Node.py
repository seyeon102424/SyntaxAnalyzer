from collections import deque


class Node:
    def __init__(self, token: str):
        self.token: str = token
        self.link: deque[Node] = deque()
        self.parse_tree: str

    def add_child(self, new_node):
        self.link.append(new_node)

    def __str__(self):
        return self.token
    
    def get_token(self)->str:
        return self.token
    
    
    def draw_Node(self, prefix="", is_last=True, is_root=True):
        if not is_root:
            print(prefix + ("└─ " if is_last else "├─ ") + str(self))
        else:
            print(str(self))
        prefix += "   " if is_last else "│  "
        child_count = len(self.link)
        for i, child in enumerate(self.link):
            is_last_child = (i == child_count - 1)
            child.draw_Node(prefix, is_last_child, False)

    def get_parse_tree_string(self, prefix="", is_last=True, is_root=True):
        self.stree_string = ""
        if not is_root:
            self.stree_string += prefix + ("└─ " if is_last else "├─ ") + str(self) + "\n"
        else:
            self.stree_string += str(self) + "\n"
        prefix += "   " if is_last else "│  "
        child_count = len(self.link)
        for i, child in enumerate(self.link):
            is_last_child = (i == child_count - 1)
            self.stree_string += child.get_parse_tree_string(prefix, is_last_child, False)
        return self.stree_string


    # def get_tree_string(self):
    #     tree_string = str(self) + '\n'
    #     self._get_tree_string_helper(self, '', True, True, tree_string)
    #     return tree_string
    
    # def _get_tree_string_helper(self, node, prefix, is_last, is_root, tree_string):
    #     if not is_root:
    #         tree_string += prefix + ("└─ " if is_last else "├─ ") + str(node) + '\n'
    #     prefix += "   " if is_last else "│  "
    #     child_count = len(node.link)
    #     for i, child in enumerate(node.link):
    #         is_last_child = (i == child_count - 1)
    #         tree_string = self._get_tree_string_helper(child, prefix, is_last_child, False, tree_string)
    #     return tree_string