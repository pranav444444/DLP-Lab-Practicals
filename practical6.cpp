#include <iostream>
#include <string>

class RecursiveDescentParser {
private:
    std::string input;
    int index;

    char current_char() {
        if (index < input.length()) {
            return input[index];
        }
        return '\0';
    }

    void consume() {
        index++;
    }

    bool parse_S() {
        if (current_char() == '(') {
            consume();
            if (parse_L()) {
                if (current_char() == ')') {
                    consume();
                    return true;
                }
            }
            return false;
        } 
        else if (current_char() == 'a') {
            consume();
            return true;
        }
        return false;
    }

    bool parse_L() {
        if (parse_S()) {
            return parse_L_prime();
        }
        return false;
    }

    bool parse_L_prime() {
        if (current_char() == ',') {
            consume();
            if (parse_S()) {
                return parse_L_prime();
            }
            return false;
        }
        return true;
    }

public:
    RecursiveDescentParser(std::string str) : input(str), index(0) {}

    bool validate() {
        bool result = parse_S();
        return result && index == input.length();
    }
};

int main() {
    int test_cases;
    std::cout << "Enter number of test cases: ";
    std::cin >> test_cases;
    std::cin.ignore();  // Ignore leftover newline from previous input

    for (int i = 0; i < test_cases; i++) {
        std::string input_string;
        std::cout << "Enter a string: ";
        std::getline(std::cin, input_string);

        RecursiveDescentParser parser(input_string);
        
        if (parser.validate()) {
            std::cout << "Valid string\n";
        } else {
            std::cout << "Invalid string\n";
        }
    }

    return 0;
}
