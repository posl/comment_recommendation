def main():
    # Get input here
    n, x = map(int, input().strip().split())
    a = []
    b = []
    for _ in range(n):
        a1, b1 = map(int, input().strip().split())
        a.append(a1)
        b.append(b1)
    # Calculate result here
    result = solve(n, x, a, b)
    # Print output here
    print("Yes" if result else "No")
