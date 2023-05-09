def main():
    # Read input
    A, B, C = map(int, input().split())
    # Solve problem
    if A**2 + B**2 < C**2:
        print('Yes')
    else:
        print('No')
