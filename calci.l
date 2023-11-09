%{
#include "calculator.tab.h"  // Include the Yacc (Bison) header file
%}

%%
[0-9]+                 { yylval.num = atoi(yytext); return NUMBER; }
"+"                    return PLUS;
"-"                    return MINUS;
"*"                    return MULTIPLY;
"/"                    return DIVIDE;
"("                    return LPAREN;
")"                    return RPAREN;
\n                     ;  // Skip newlines
[ \t]                  ;  // Skip spaces and tabs
.                      return *yytext;
%%

int main() {
    yyparse();
    return 0;
}
