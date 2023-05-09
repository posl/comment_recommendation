def main():
    # Read input
    A, B, C = map(int, input().split())
    # Calculate and print output
    print(max(A + B + C, A * B * C, (A + B) * C, A * (B + C)))
