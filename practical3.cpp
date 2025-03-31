#include <iostream>
#include <cctype>
#include <unordered_set>
#include <unordered_map>
#include <regex>
using namespace std;

unordered_set<string> keywords = {"auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "inline", "int", "long", "register", "return", "short", "signed",
    "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned",
    "void", "volatile", "while"};

unordered_set<string> symbolTable;
unordered_set<string> functions;

bool isKeyword(const string& str) {
    return keywords.find(str) != keywords.end();
}

bool isOperator(char c) {
    string ops = "+-*/%=<>!&|";
    return ops.find(c) != string::npos;
}

string removeComments(const string& code) {
    string cleanedCode;
    bool inBlockComment = false, inLineComment = false;
    for (size_t i = 0; i < code.length(); i++) {
        if (inBlockComment && code[i] == '*' && code[i + 1] == '/') {
            inBlockComment = false; i++;
        } 
        else if (inLineComment && code[i] == '\n') {
            inLineComment = false;
        } 
        else if (!inBlockComment && !inLineComment) {
            if (code[i] == '/' && code[i + 1] == '*') {
                inBlockComment = true; i++;
            } 
            else if (code[i] == '/' && code[i + 1] == '/') {
                inLineComment = true; i++;
            } 
            else {
                cleanedCode += code[i];
            }
        }
    }
    return cleanedCode;
}

void tokenize(string code) {
    string token;
    code = removeComments(code);
    for (size_t i = 0; i < code.length(); i++) {
        char c = code[i];
        
        if (isspace(c)) continue;
        
        if (isalpha(c) || c == '_') {
            token.clear();
            while (isalnum(code[i]) || code[i] == '_') {
                token += code[i];
                i++;
            }
            i--;
            if (isKeyword(token)) {
                cout << "Keyword: " << token << endl;
            } 
            else if (token != "main") {  
                symbolTable.insert(token);
                cout << "Identifier: " << token << endl;
            }
             else {
                cout << "Identifier: " << token << endl;
            }
        }
        
        else if (isdigit(c)) {
            token.clear();
            while (isalnum(code[i])) {
                token += code[i];
                i++;
            }
            i--;
            if (regex_match(token, regex("[0-9]+"))) {
                cout << "Constant: " << token << endl;
            } 
            else {
                cout << "Lexical Error: " << token << " invalid lexeme" << endl;
            }
        }
        
        else if (c == '\'') {
            token.clear();
            token += c;
            i++;
            if (code[i] != '\'' || code[i + 1] != ';') {
                token += code[i];
                if (code[i + 1] == '\'') {
                    token += code[i + 1];
                    i++;
                    cout << "String: " << token << endl;
                } 
                else {
                    cout << "Lexical Error: Invalid character literal" << endl;
                }
            }
            i++;
        }
        
        else if (isOperator(c)) {
            token.clear();
            token += c;
            if (isOperator(code[i + 1])) {
                token += code[i + 1];
                i++;
            }
            cout << "Operator: " << token << endl;
        }
        
        else if (ispunct(c)) {
            cout << "Punctuation: " << c << endl;
        }
        
        else {
            cout << "Lexical Error: " << c << " invalid lexeme" << endl;
        }
    }
}

int main() {
    string code, line;
    cout << "Enter your code and write END at last to Terminate: " << endl;
    while (getline(cin, line)) {
        if (line == "END") {
            break;
        }
        code += line + "\n";
    }
    
    cout << "\nTokenized Output:\n";
    tokenize(code);
    
    cout << "\nSymbol Table:\n";
    for (const auto& entry : symbolTable) {
        cout << entry << endl;
    }
    
    return 0;
}

