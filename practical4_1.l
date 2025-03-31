%{
#include <stdio.h>
%}

%%
[0-9]+    { printf("%s\n", yytext); }  // Print numbers
.|\n      { /* Ignore everything else */ }

%%

int main() {
    yylex();  // Start lexical analysis
    return 0;
}

int yywrap() {
    return 1;
}




