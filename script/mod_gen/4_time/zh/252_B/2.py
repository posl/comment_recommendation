def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = set(a)
    y = set(b)
    z = x & y
    if len(z) >= 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()