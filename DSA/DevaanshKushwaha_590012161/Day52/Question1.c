#include <stdio.h>
int main() {
    int n, x;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    scanf("%d", &x);
    int l = 0, r = n - 1, found = 0;
    while (l < r) {
        int sum = arr[l] + arr[r];
        if (sum == x) {
            found = 1;
            break;
        } else if (sum < x) l++;
        else r--;
    }
    if (found) printf("true");
    else printf("false");
}
