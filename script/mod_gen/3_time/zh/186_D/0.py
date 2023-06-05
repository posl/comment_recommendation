def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    x = 0
    for i in range(n):
        s -= a[i]
        x += a[i] * s
    print(x)

if __name__ == '__main__':
    main()