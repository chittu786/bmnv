%{
#include <stdio.h>
int charCount = 0;
int wordCount = 0;
int lineCount = 0;
%}

%%
[a-zA-Z]+   { wordCount++; }
\n          { lineCount++; }
.           { charCount++; }
%%

int main() {
    yylex();
    printf("Character count: %d\n", charCount);
    printf("Word count: %d\n", wordCount);
    printf("Line count: %d\n", lineCount);
    return 0;
}
