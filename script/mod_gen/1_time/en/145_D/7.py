def main():
    # Read input
    X, Y = map(int, input().split())
    # Check if (X, Y) is reachable from (0, 0)
    if (X + Y) % 3 != 0:
        print(0)
        return
    # Calculate n and m
    n = (X + Y) // 3
    m = X - n
    # Check if (X, Y) is reachable from (0, 0)
    if m < 0 or m > n:
        print(0)
        return
    # Calculate the number of ways
    print(combination(n, m))

if __name__ == '__main__':
    main()