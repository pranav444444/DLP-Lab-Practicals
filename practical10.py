import re
import operator

def evaluate_expression(expression: str):
    try:
        # Validate the expression (allow only numbers, operators, and parentheses)
        if not re.fullmatch(r"[0-9+\-*/^(). ]+", expression):
            return "Invalid expression"
        
        # Define operator precedence and associativity
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}
        
        def apply_operator(values, op):
            right = values.pop()
            left = values.pop()
            operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
            values.append(operations[op](left, right))
        
        def shunting_yard(expression):
            output = []
            operators = []
            tokens = re.findall(r"\d+\.?\d*|[+\-*/^()]", expression)
            
            for token in tokens:
                if re.match(r"\d+\.?\d*", token):
                    output.append(float(token))
                elif token in precedence:
                    while (operators and operators[-1] != '(' and
                           (precedence[operators[-1]] > precedence[token] or
                            (precedence[operators[-1]] == precedence[token] and associativity[token] == 'L'))):
                        output.append(operators.pop())
                    operators.append(token)
                elif token == '(':
                    operators.append(token)
                elif token == ')':
                    while operators and operators[-1] != '(':
                        output.append(operators.pop())
                    if operators and operators[-1] == '(':
                        operators.pop()
                    else:
                        return "Invalid expression"
            
            while operators:
                if operators[-1] in "()":
                    return "Invalid expression"
                output.append(operators.pop())
            
            return output
        
        def evaluate_rpn(rpn):
            stack = []
            for token in rpn:
                if isinstance(token, float):
                    stack.append(token)
                else:
                    apply_operator(stack, token)
            return stack[0] if len(stack) == 1 else "Invalid expression"
        
        rpn = shunting_yard(expression)
        if isinstance(rpn, str):
            return rpn
        return evaluate_rpn(rpn)
    except Exception as e:
        return f"Invalid expression: {str(e)}"

# Get number of test cases
num_cases = int(input("Enter number of test cases: "))

for _ in range(num_cases):
    expr = input("Enter expression: ")
    print(f"Output: {evaluate_expression(expr)}\n")

