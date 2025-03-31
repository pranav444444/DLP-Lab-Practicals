def compute_first_sets(productions):
    first_sets = {non_terminal: set() for non_terminal in productions}
    changed = True

    while changed:
        changed = False

        for non_terminal, rules in productions.items():
            for production in rules:
                for ch in production.split():
                    if not ch.isupper():
                        if ch not in first_sets[non_terminal]:
                            first_sets[non_terminal].add(ch)
                            changed = True
                        break
                    else:
                        if 'ε' in first_sets[ch]:
                            if 'ε' not in first_sets[non_terminal]:
                                first_sets[non_terminal].add('ε')
                                changed = True
                            continue
                        else:
                            for terminal in first_sets[ch]:
                                if terminal not in first_sets[non_terminal]:
                                    first_sets[non_terminal].add(terminal)
                                    changed = True
                            break
    return first_sets

def compute_follow_sets(productions, first_sets):
    follow_sets = {non_terminal: set() for non_terminal in productions}
    follow_sets['S'].add('$')
    changed = True

    while changed:
        changed = False

        for non_terminal, rules in productions.items():
            for production in rules:
                next_follow = set(follow_sets[non_terminal])

                for symbol in reversed(production.split()):
                    if symbol.isupper():
                        for terminal in next_follow:
                            if terminal not in follow_sets[symbol]:
                                follow_sets[symbol].add(terminal)
                                changed = True

                        if 'ε' in first_sets[symbol]:
                            next_follow.update(follow_sets[non_terminal])
                        else:
                            next_follow = first_sets[symbol].copy()
                    else:
                        next_follow = {symbol}
    return follow_sets

def main():
    productions = {
        'S': ['A B C', 'D'],
        'A': ['a', 'ε'],
        'B': ['b', 'ε'],
        'C': ['( S )', 'c'],
        'D': ['A C']
    }

    first_sets = compute_first_sets(productions)
    follow_sets = compute_follow_sets(productions, first_sets)

    print("First Sets:")
    for non_terminal, terminals in first_sets.items():
        print(f"First({non_terminal}) = {{ {', '.join(terminals)} }}")

    print("\nFollow Sets:")
    for non_terminal, terminals in follow_sets.items():
        print(f"Follow({non_terminal}) = {{ {', '.join(terminals)} }}")

if __name__ == "__main__":
    main()
