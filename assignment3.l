%{
#include <stdio.h>
#include <string.h>
int ctr = 0, word = 0, line = 0;
%}
%option noyywrap
%%
[a-zA-Z]+   { word++; ctr += yyleng; }     // Action 1: Count word and characters
\n          { line++; ctr++; }             // Action 2: Count line and newline character
.           { ctr++; }                     // Action 3: Count all other characters
%%
int main(){
    yylex();
    printf("lines: %d, words: %d, characters: %d\n",
           line, word, ctr);
    return 0;
}
