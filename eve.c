#include <stdio.h>
#include <string.h>

struct op {
    char l;
    char r[20];
} op[10], pr[10];

int main() {
    int i, j, n, z = 0;
    char *p;
    char temp;

    printf("Enter the Number of Values: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("left: ");
        scanf(" %c", &op[i].l);
        printf("\tright: ");
        scanf("%s", op[i].r);
    }

    printf("Intermediate Code\n");
    for (i = 0; i < n; i++) {
        printf("%c=%s\n", op[i].l, op[i].r);
    }

    for (i = 0; i < n - 1; i++) {
        temp = op[i].l;
        for (j = 0; j < n; j++) {
            p = strchr(op[j].r, temp);
            if (p) {
                pr[z].l = op[i].l;
                strcpy(pr[z].r, op[i].r);
                z++;
            }
        }
    }

    pr[z].l = op[n - 1].l;
    strcpy(pr[z].r, op[n - 1].r);
    z++;

    printf("\nAfter Dead Code Elimination\n");
    for (int k = 0; k < z; k++) {
        printf("%c=%s\n", pr[k].l, pr[k].r);
    }

    return 0;
}
