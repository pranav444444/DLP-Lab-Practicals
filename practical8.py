import collections

def compute_first_follow():
    first = {
        'S': {'a', 'b', '(', 'c'},
        'A': {'a', ''},
        'B': {'b', ''},
        'C': {'(', 'c'},
        'D': {'a', '('},
    }
    
    follow = {
        'S': {')', '$'},
        'A': {'b', '(', ')', '$'},
        'B': {'c', ')', '$'},
        'C': {')', '$'},
        'D': {')', '$'},
    }
    
    terminals = {'a', 'b', 'c', '(', ')', '$'}
    
    return first, follow, terminals

def construct_parsing_table(first, follow, terminals):
    table = collections.defaultdict(dict)
    grammar = {
        'S': ['A B C', 'D'],
        'A': ['a', 'ε'],
        'B': ['b', 'ε'],
        'C': ['( S )', 'c'],
        'D': ['A C']
    }
    
    for non_terminal, productions in grammar.items():
        for production in productions:
            first_set = set()
            if production == 'ε':
                first_set = follow[non_terminal]
            else:
                for symbol in production.split():
                    if symbol in terminals:
                        first_set.add(symbol)
                        break
                    first_set |= first.get(symbol, {symbol})
                    if 'ε' not in first[symbol]:
                        break
            
            for terminal in first_set - {'ε'}:
                table[non_terminal][terminal] = production
            
            if 'ε' in first_set:
                for terminal in follow[non_terminal]:
                    table[non_terminal][terminal] = production
    
    return table

def is_ll1(parsing_table):
    for non_terminal in parsing_table:
        terminals = list(parsing_table[non_terminal].keys())
        if len(terminals) != len(set(terminals)):
            return False
    return True

def validate_string(parsing_table, input_string):
    stack = ['$', 'S']
    input_string += '$'
    i = 0
    
    while stack:
        top = stack.pop()
        if top == input_string[i]:
            i += 1
        elif top in parsing_table:
            if input_string[i] in parsing_table[top]:
                production = parsing_table[top][input_string[i]].split()
                if production == ['ε']:
                    continue
                stack.extend(reversed(production))
            else:
                return "Invalid string"
        else:
            return "Invalid string"
    
    return "Valid string" if i == len(input_string) else "Invalid string"

def main():
    first, follow, terminals = compute_first_follow()
    parsing_table = construct_parsing_table(first, follow, terminals)
    
    print("Predictive Parsing Table:")
    for nt, rules in parsing_table.items():
        print(nt, "->", rules)
    
    if is_ll1(parsing_table):
        print("The grammar is LL(1)")
    else:
        print("The grammar is NOT LL(1)")
    
    num_tests = int(input("Enter number of test cases: "))
    for _ in range(num_tests):
        test_string = input("Enter a string: ")
        print(validate_string(parsing_table, test_string))

if __name__ == "__main__":
    main()

