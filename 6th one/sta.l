%%
^[Aa].*  printf("string with a : %s\n" , yytext);
.
\n
%%

int main() {
	yylex();
	return 0;
}
