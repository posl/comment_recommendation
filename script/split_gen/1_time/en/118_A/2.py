def main():
    # Read the input
    A, B = map(int, input().split())
    # Check if A is a divisor of B
    if B % A == 0:
        # If A is a divisor of B, print A + B
        print(A + B)
    else:
        # If A is not a divisor of B, print B - A
        print(B - A)
