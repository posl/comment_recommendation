def main():
    n, x = map(int, input().split())
    total = 0
    for _ in range(n):
        a, b = map(int, input().split())
        total += a * b
    if total > x:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()