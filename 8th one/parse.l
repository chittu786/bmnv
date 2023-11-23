%{
#include <stdio.h>
#include "y.tab.h"
extern int yylval;
%}

%%
0       { yylval = 0; return Zero; }
1       { yylval = 1; return One; }
[\t]    { /* ignore whitespace */ }
.       { return yytext[0]; }
%%

int yywrap() {
    return 1;
}

