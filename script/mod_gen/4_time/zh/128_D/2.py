def main():
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    ans = 0
    for i in range(n+1):
        for j in range(n+1):
            if i+j > k:
                continue
            r = k - i - j
            t = []
            for l in range(i):
                t.append(v[l])
            for l in range(n-j,n):
                t.append(v[l])
            t.sort()
            for l in range(r):
                if len(t) == 0:
                    break
                if t[0] > 0:
                    break
                t.pop(0)
            ans = max(ans,sum(t))
    print(ans)

if __name__ == '__main__':
    main()