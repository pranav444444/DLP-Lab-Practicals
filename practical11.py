import re

class Parser:
    def __init__(self, text):
        self.tokens = self.tokenize(text)
        self.pos = 0
        self.quadruples = []
        self.temp_counter = 1

    def tokenize(self, text):
        token_pattern = r'\d+\.\d+|\d+|[+\-*/()]'
        tokens = re.findall(token_pattern, text)
        return tokens

    def new_temp(self):
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token):
        if self.current_token() == token:
            self.pos += 1
        else:
            raise Exception(f"Unexpected token: Expected {token} but found {self.current_token()}")

    def parse_E(self):
        left = self.parse_T()
        while self.current_token() in ('+', '-'):
            op = self.current_token()
            self.eat(op)
            right = self.parse_T()
            temp = self.new_temp()
            self.quadruples.append((op, left, right, temp))
            left = temp
        return left

    def parse_T(self):
        left = self.parse_F()
        while self.current_token() in ('*', '/'):
            op = self.current_token()
            self.eat(op)
            right = self.parse_F()
            temp = self.new_temp()
            self.quadruples.append((op, left, right, temp))
            left = temp
        return left

    def parse_F(self):
        token = self.current_token()
        if token is None:
            raise Exception("Unexpected end of expression")
        if token == '(':
            self.eat('(')
            result = self.parse_E()
            self.eat(')')
            return result
        else:
            self.eat(token)
            return token

def main():
    testcases = int(input("Enter number of testcases: "))
    for _ in range(testcases):
        expr = input("\nEnter arithmetic expression: ")
        parser = Parser(expr)
        final_result = parser.parse_E()
        if parser.pos != len(parser.tokens):
            raise Exception("Extra tokens remaining after parsing")
    
        print("\nOperator\tOperand1\tOperand2\tResult")
        for quad in parser.quadruples:
            op, operand1, operand2, result = quad
            print(f"{op}\t\t{operand1}\t\t{operand2}\t\t{result}")
    
        print("\nFinal result is stored in:", final_result)

if __name__ == "__main__":
    main()


