# Six-Digit Security Code

A company creates a six-digit security code from a five-digit employee number, given as five separate digits:

- `digit_1 = 8`
- `digit_2 = 3`
- `digit_3 = 7`
- `digit_4 = 2`
- `digit_5 = 4`

Write a Python program that creates a check digit using the following rules:

1. Multiply `digit_1` by 2.
2. Multiply `digit_2` by 3.
3. Multiply `digit_3` by 4.
4. Multiply `digit_4` by 5.
5. Multiply `digit_5` by 6.
6. Add all five results together.
7. The check digit is the remainder when this sum is divided by 10.

Write a function called `check_digit()` that takes the five digits as arguments and returns the check digit.

Finally, print the original five-digit employee number followed by its check digit.

For the values above, the program should produce the complete six-digit security code.

## Purpose of the Problem

This problem is meant to test the understanding of variables and modular arithmetic. I chose modular arithmetic because using the remainder operator is difficult for me to understand. The problem requires performing several calculations, combining the results, and creating a check digit.

For me, it is hard to understand why `% 10` gives the final digit and how to combine all separate parts into one answer.