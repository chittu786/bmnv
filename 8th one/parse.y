%{
#include <stdio.h>
#include <stdlib.h>
#include "y.tab.h"
void yyerror(const char *s);
int yylex(void);
%}

%token Zero One

%%
stmt: S { printf("Accepted\n"); exit(0); };

S   : S A | A;

A   : Zero Zero | One One;
%%

int main() {
    yyparse();
    printf("Not Accepted\n");
    exit(0);
}

void yyerror(const char *s) {
    printf("Not Accepted\n");
    exit(0);
}

