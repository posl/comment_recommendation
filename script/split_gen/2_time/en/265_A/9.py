def main():
    # Read from Standard Input
    x, y, n = map(int, input().split())
    # Solve the problem
    ans = 0
    if n % 3 == 0:
        ans = (n // 3) * y
    elif n % 3 == 1:
        ans = ((n - 1) // 3) * y + x
    elif n % 3 == 2:
        ans = ((n - 2) // 3) * y + 2 * x
    # Print the answer to Standard Output
    print(ans)
