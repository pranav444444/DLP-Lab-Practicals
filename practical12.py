import re

class Num:
    def __init__(self, value):
        self.value = value

class Var:
    def __init__(self, name):
        self.name = name

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Parser:
    def __init__(self, text):
        self.tokens = self.tokenize(text)
        self.pos = 0

    def tokenize(self, text):
        pattern = r'\d+\.\d+|\d+|[a-zA-Z_]\w*|[+\-*/()]'
        tokens = re.findall(pattern, text)
        return tokens

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token):
        if self.current_token() == token:
            self.pos += 1
        else:
            raise Exception(f"Expected {token} but found {self.current_token()}")

    def parse(self):
        node = self.parse_E()
        if self.pos != len(self.tokens):
            raise Exception("Extra tokens remaining after parsing")
        return node

    def parse_E(self):
        node = self.parse_T()
        while self.current_token() in ('+', '-'):
            op = self.current_token()
            self.eat(op)
            right = self.parse_T()
            node = BinOp(node, op, right)
        return node

    def parse_T(self):
        node = self.parse_F()
        while self.current_token() in ('*', '/'):
            op = self.current_token()
            self.eat(op)
            right = self.parse_F()
            node = BinOp(node, op, right)
        return node

    def parse_F(self):
        token = self.current_token()
        if token is None:
            raise Exception("Unexpected end of expression")
        if token == '(':
            self.eat('(')
            node = self.parse_E()
            self.eat(')')
            return node
        elif re.match(r'\d+\.\d+|\d+', token):
            self.eat(token)
            if '.' in token:
                return Num(float(token))
            else:
                return Num(int(token))
        elif re.match(r'[a-zA-Z_]\w*', token):
            self.eat(token)
            return Var(token)
        else:
            raise Exception(f"Invalid token {token}")

def fold_constants(node):
    if isinstance(node, BinOp):
        left = fold_constants(node.left)
        right = fold_constants(node.right)
        if isinstance(left, Num) and isinstance(right, Num):
            if node.op == '+':
                return Num(left.value + right.value)
            elif node.op == '-':
                return Num(left.value - right.value)
            elif node.op == '*':
                return Num(left.value * right.value)
            elif node.op == '/':
                return Num(left.value / right.value)
        return BinOp(left, node.op, right)
    return node

precedence = {'+':1, '-':1, '*':2, '/':2}

def ast_to_str(node, parent_prec=0):
    if isinstance(node, Num):
        return str(node.value)
    elif isinstance(node, Var):
        return node.name
    elif isinstance(node, BinOp):
        curr_prec = precedence[node.op]
        left_str = ast_to_str(node.left, curr_prec)
        right_str = ast_to_str(node.right, curr_prec + 1)
        s = f"{left_str} {node.op} {right_str}"
        if curr_prec < parent_prec:
            s = f"({s})"
        return s

def main():
    testcases = int(input("Enter number of testcases: "))
    for _ in range(testcases):
        expr = input("Enter arithmetic expression: ")
        parser = Parser(expr)
        ast = parser.parse()
        optimized_ast = fold_constants(ast)
        optimized_expr = ast_to_str(optimized_ast)
        print("Optimized expression:")
        print(optimized_expr)
        print()

if __name__ == "__main__":
    main()

