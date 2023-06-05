def main():
    n,k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for l in range(min(n,k)+1):
        for r in range(min(n,k)-l+1):
            if l+r > n:
                continue
            t = []
            for i in range(l):
                t.append(v[i])
            for i in range(n-r,n):
                t.append(v[i])
            t.sort()
            s = 0
            for i in range(len(t)):
                if t[i] < 0 and i < k-l-r:
                    continue
                s += t[i]
            ans = max(ans,s)
    print(ans)

if __name__ == '__main__':
    main()