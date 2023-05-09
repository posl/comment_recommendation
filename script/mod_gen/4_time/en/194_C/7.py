def main():
    n = int(input())
    a = list(map(int, input().split()))
    t = sum(a)
    s = 0
    for i in range(n):
        t -= a[i]
        s += t*a[i]
    print(s)

if __name__ == '__main__':
    main()