%{
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void printToken(const char* type, const char* value) {
    printf("%s: %s\n", type, value);
}
%}

KEYWORDS     "int"|"char"|"return"|"if"|"else"|"for"|"while"|"do"|"switch"|"case"|"break"|"continue"|"void"|"float"|"double"
IDENTIFIER   [a-zA-Z_][a-zA-Z0-9_]*
CONSTANT     [0-9]+
STRING       \'[^']\'|\"[^\"]*\"
OPERATOR     \+|\-|\*|\/|=|==|!=|<|>|<=|>=|&&|\|\|
PUNCTUATION  [\(\)\{\}\[\],;]
COMMENT      \/\/.|\/\([^]|\+[^\/])\+\/

%%
{KEYWORDS}       { printToken("Keyword", yytext); }
{IDENTIFIER}     { printToken("Identifier", yytext); }
{CONSTANT}       { printToken("Constant", yytext); }
{STRING}         { printToken("String", yytext); }
{OPERATOR}       { printToken("Operator", yytext); }
{PUNCTUATION}    { printToken("Punctuation", yytext); }
{COMMENT}        { /* Ignore comments */ }
[ \t\n]+         { /* Ignore white spaces */ }
.                { printToken("Lexical Error", yytext); } // Detect invalid tokens
%%

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <C source file>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        printf("Error: Cannot open file %s\n", argv[1]);
        return 1;
    }

    yyin = file;  // Set input file for Lex
    yylex();      // Process file
    fclose(file); // Close file

    return 0;
}

int yywrap() {
    return 1;
}
