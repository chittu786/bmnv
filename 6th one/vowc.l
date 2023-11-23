%{
#include <stdio.h>
int vowelCount = 0;
int consonantCount = 0;
%}

%%
[aeiouAEIOU]    { vowelCount++; }
[a-zA-Z]        { consonantCount++; }
[ \t\n]         ;  /* Ignore whitespace */
.               ;  /* Ignore other characters */

%%

int main() {
    yylex();
    printf("Vowel Count: %d\n", vowelCount);
    printf("Consonant Count: %d\n", consonantCount);
    return 0;
}
