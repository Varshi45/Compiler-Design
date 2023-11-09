%{
#include "c_parser.tab.h"  // Include the Yacc (Bison) header file
%}

%%
[a-zA-Z_][a-zA-Z0-9_]*   { yylval.strval = strdup(yytext); return ID; }
[0-9]+                  { yylval.intval = atoi(yytext); return NUM; }
"if"                    return IF;
"else"                  return ELSE;
"while"                 return WHILE;
"+"                     return PLUS;
"-"                     return MINUS;
"*"                     return MULT;
"/"                     return DIV;
"="                     return ASSIGN;
"=="                    return EQ;
"!="                    return NE;
"<"                     return LT;
">"                     return GT;
"<="                    return LE;
">="                    return GE;
"("                     return LPAREN;
")"                     return RPAREN;
"{"                     return LBRACE;
"}"                     return RBRACE;
";"                     return SEMICOLON;
.                       return yytext[0];
%%

int main(int argc, char* argv[]) {
    yylex();
    return 0;
}
