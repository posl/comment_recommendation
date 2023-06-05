def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    for i in range(n):
        s += (a[i] * i - a[i] * (n - 1 - i))
    print(s)

if __name__ == '__main__':
    main()