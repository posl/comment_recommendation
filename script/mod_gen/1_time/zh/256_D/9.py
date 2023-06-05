def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        ll, rr = map(int, input().split())
        l.append(ll)
        r.append(rr)
    l.sort()
    r.sort()
    l.append(0)
    r.append(0)
    ans = 0
    for i in range(n):
        if l[i+1] > r[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()