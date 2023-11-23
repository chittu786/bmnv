%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}

%token NUM

%%
calc: /* empty */
    | calc expr '\n' { printf("Result: %d\n", $2); }
    ;

expr: NUM           { $$ = $1; }
    | expr '+' NUM  { $$ = $1 + $3; }
    | expr '-' NUM  { $$ = $1 - $3; }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}
