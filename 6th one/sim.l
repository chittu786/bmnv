%{
#include<stdio.h>
%}

%option noyywrap

DIGIT    [0-9]
LETTER   [a-zA-Z]
NUM      {DIGIT}+(\.{DIGIT}+)?(E[+-]?{DIGIT}+)?

%%
"if"       { printf("keyword: if\n"); }
"else"     { printf("keyword: else\n"); }
"while"    { printf("keyword: while\n"); }
"int"      { printf("keyword: int\n"); }
"float"    { printf("keyword: float\n"); }
{LETTER}({LETTER}|{DIGIT})*   { printf("Identifier: %s\n", yytext); }
{NUM}      { printf("Number: %s\n", yytext); }
[ \t\n]    ; // skip whitespace
.          { printf("Invalid: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}
