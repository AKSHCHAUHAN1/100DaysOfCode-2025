
#include <stdio.h>
#include <string.h>

int isRotation(char str1[], char str2[]) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    if (len1 != len2) return 0;

    char temp[2 * len1 + 1];
    strcpy(temp, str1);
    strcat(temp, str1);

    return strstr(temp, str2) != NULL;
}

int main() {
    char str1[100], str2[100];
    scanf("%s %s", str1, str2);
    if (isRotation(str1, str2))
        printf("true\n");
    else
        printf("false\n");
    return 0;
}
