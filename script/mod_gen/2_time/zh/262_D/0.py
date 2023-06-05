def main():
    n = int(raw_input())
    a = [int(i) for i in raw_input().split()]
    a = [0] + a
    ans = 0
    for i in xrange(1, n + 1):
        if a[a[i]] == i:
            ans += 1
    print ans / 2

if __name__ == '__main__':
    main()