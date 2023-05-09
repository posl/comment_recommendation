def main():
    # Get the input
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # Process
    total = 0
    for i in range(n):
        if i % 2 == 1:
            total += a[i] - 1
        else:
            total += a[i]
    # Output
    if total <= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()