def main():
    # Read input
    A, B, T = map(int, input().split())
    # Compute answer
    answer = B * (T // A)
    # Print answer
    print(answer)
