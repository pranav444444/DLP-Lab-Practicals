%{
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int length = 0, has_lower = 0, has_upper = 0, has_digit = 0, has_symbol = 0;
%}

%%
[a-z]       { has_lower = 1; length++; }   // At least one lowercase letter
[A-Z]       { has_upper = 1; length++; }   // At least one uppercase letter
[0-9]       { has_digit = 1; length++; }   // At least one digit
[*;#$@]     { has_symbol = 1; length++; }  // At least one special symbol
.           { length++; }                  // Count all characters
\n          { 
                if (length >= 9 && length <= 15 && has_lower && has_upper && has_digit && has_symbol) {
                    printf("Valid Password\n");
                } else {
                    printf("Invalid Password\n");
                }
                length = 0; has_lower = 0; has_upper = 0; has_digit = 0; has_symbol = 0;
            }
%%

int main() {
    printf("Enter password: ");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
