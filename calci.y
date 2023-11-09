%{
#include <stdio.h>
#include <math.h>
%}

%token NUMBER PLUS MINUS MULTIPLY DIVIDE LPAREN RPAREN

%%
input: /* empty */
     | input line
     ;

line: expr '\n' { printf("Result: %f\n", $1); }
    ;

expr: term            { $$ = $1; }
    | expr PLUS term  { $$ = $1 + $3; }
    | expr MINUS term { $$ = $1 - $3; }
    ;

term: factor              { $$ = $1; }
    | term MULTIPLY factor { $$ = $1 * $3; }
    | term DIVIDE factor   { $$ = $1 / $3; }
    ;

factor: NUMBER           { $$ = $1; }
      | LPAREN expr RPAREN { $$ = $2; }
      | MINUS factor      { $$ = -1 * $2; }
      ;

%%

int yylex() {
    return yylex_wrap();
}

int yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}

int main() {
    yyparse();
    return 0;
}
