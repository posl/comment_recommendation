def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    if k > n:
        print(-1)
        return
    a.sort()
    a.reverse()
    if d == 1:
        print(a[0])
        return
    s = set()
    for i in range(n-k+1):
        s.add(sum(a[i:i+k]))
    s = list(s)
    s.sort()
    s.reverse()
    for x in s:
        if x % d == 0:
            print(x)
            return
    print(-1)
main()

if __name__ == '__main__':
    main()