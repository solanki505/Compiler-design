/*Design a scanner without using flex) for the following set of tokens.
{a, b, ab, aab, abb, aaa, baab, aabba, bbaba}.

An input to the scanner is an element of {a, b}

+ terminated by ‘c’. There may

be blanks (‘ ’) as separators in between strings of {a, b}
+ e.g.

bababba ab babaa bbabbabc.*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// List of valid tokens
const char *tokens[] = {
    "a", "b", "ab", "aab", "abb", "aaa", "baab", "aabba", "bbaba"
};
const int num_tokens = sizeof(tokens) / sizeof(tokens[0]);

// Function to check if str matches a token
int is_token(const char *str) {
    for (int i = 0; i < num_tokens; i++) {
        if (strcmp(str, tokens[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to perform maximal matching
void match_tokens(const char *input) {
    int len = strlen(input);
    int i = 0;

    while (i < len) {
        // Skip blanks
        if (isspace(input[i])) {
            i++;
            continue;
        }

        if (input[i] == 'c') break; // End of input

        int maxlen = 0;
        char best_match[10] = "";

        // Try every prefix up to max 5 characters
        for (int l = 1; l <= 5 && i + l <= len; l++) {
            char substr[10];
            strncpy(substr, &input[i], l);
            substr[l] = '\0';

            if (is_token(substr)) {
                if (l > maxlen) {
                    maxlen = l;
                    strcpy(best_match, substr);
                }
            }
        }

        if (maxlen > 0) {
            printf("< %s > ", best_match);
            i += maxlen;
        } else {
            // Unknown character, skip
            i++;
        }
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <inputfile>\n", argv[0]);
        return 1;
    }

    FILE *fp = fopen(argv[1], "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }

    char buffer[1000];
    fgets(buffer, sizeof(buffer), fp);
    fclose(fp);

    match_tokens(buffer);
    return 0;
}


