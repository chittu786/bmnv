#include <stdio.h>

int main() {
    int n, i;
    char op, arg1, arg2, result;

    printf("Enter the number of three-address codes: ");
    scanf("%d", &n);
    printf("Enter the three-address codes:\n");

    for (i = 0; i < n; i++) {
        // Assuming a space-separated input format (e.g., a = b + c)
        scanf(" %c = %c %c %c", &result, &arg1, &op, &arg2);
        printf("The generated code is:\n");
        // Code generation
        printf("Mov %c, %c\n", arg1, result);

        switch (op) {
            case '+':
                printf("Add %c, %c\n", arg2, result);
                break;
            case '-':
                printf("Sub %c, %c\n", arg2, result);
                break;
            case '*':
                printf("Mul %c, %c\n", arg2, result);
                break;
            case '/':
                printf("Div %c, %c\n", arg2, result);
                break;
            default:
                printf("Unsupported operation: %c\n", op);
                break;
        }

        printf("\n");
    }

    return 0;
}
