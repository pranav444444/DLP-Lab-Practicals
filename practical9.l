YACC code:
%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(const char *s);
int yylex();
%}

%token IF ELSE A B T

%%

S       : IF E T S S_prime { printf("Valid string\n"); }
        | A { printf("Valid string\n"); }
        ;

S_prime : ELSE S
        | /* epsilon */ 
        ;

E       : B 
        ;

%%

void yyerror(const char *s) {
    printf("Invalid string\n");
}

int main() {
    printf("Enter the input string:\n");
    yyparse();
    return 0;
}

Lex Code:
%{
#include "y.tab.h"
%}

%%
if      { return IF; }
else    { return ELSE; }
a       { return A; }
b       { return B; }
t       { return T; }
[ \t\n] ;  // Ignore spaces, tabs, and newlines
.       { return yytext[0]; }
%%

