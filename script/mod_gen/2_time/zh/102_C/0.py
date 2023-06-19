def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    a.sort()
    ans = 10 ** 18
    for i in xrange(-1, 2):
        b = a[n/2] + i
        tmp = 0
        for j in xrange(n):
            tmp += abs(a[j] - (b + j + 1))
        ans = min(ans, tmp)
    print ans

if __name__ == '__main__':
    main()