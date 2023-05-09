def main():
    # Input
    N = int(input())
    # Initialize
    S = ''
    # Process
    while N > 0:
        if N % 2 == 0:
            S = 'B' + S
            N //= 2
        else:
            S = 'A' + S
            N -= 1
    # Output
    print(S)
