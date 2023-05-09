def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    t = 0
    min_d = 10**18
    for i in range(n-1):
        t += a[i]
        if min_d > abs(s - 2*t):
            min_d = abs(s - 2*t)
    print(min_d)

if __name__ == '__main__':
    main()