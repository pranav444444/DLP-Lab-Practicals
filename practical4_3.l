%{
#include <stdio.h>

int char_count = 0, word_count = 0, line_count = 0;
%}

%%
.       { char_count++; }  // Count each character
\n      { line_count++; char_count++; }  // Count newline as a character
[ \t]+  { /* Ignore spaces and tabs */ }
[^\n \t]+ { word_count++; }  // Count words (sequences of non-space, non-tab characters)
%%

int main() {
    yylex();
    printf("\nCharacters: %d\n", char_count);
    printf("Words: %d\n", word_count);
    printf("Lines: %d\n", line_count);
    return 0;
}

int yywrap() {
    return 1;
}
