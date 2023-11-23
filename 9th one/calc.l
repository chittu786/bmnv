%{
#include "y.tab.h"
void yyerror(const char *s);
%}

%%
[0-9]+    { yylval = atoi(yytext); return NUM; }
[-+*/\n]  { return yytext[0]; }
[ \t]     { /* ignore whitespace */ }
.         { yyerror("Invalid character"); }
%%

int yywrap() {
    return 1;
}


