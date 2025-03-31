#include <stdio.h>
#include <string.h>

int main() {
    int n;
    printf("Enter no. of testcases: ");
    scanf("%d", &n);

    while (n > 0) {
        char s[20];  // Increased buffer size
        printf("Enter the string: ");
        scanf("%19s", s);  // Avoids buffer overflow
        int len = strlen(s);

        int i = 0;
        while (i < len && s[i] == 'a') {
            i++;
        }

        if (i < len - 1 && s[i] == 'b' && s[i + 1] == 'b' && s[i + 2] == '\0') {
            printf("String Accepted!!!\n");
        } else {
            printf("String Rejected!!!\n");
        }

        n--;
    }
    return 0;
}
