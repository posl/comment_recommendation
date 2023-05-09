def main():
    A, B, Q = map(int, input().split())
    s = [-float('inf')] + [int(input()) for _ in range(A)] + [float('inf')]
    t = [-float('inf')] + [int(input()) for _ in range(B)] + [float('inf')]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        si = bisect.bisect_left(s, x[i])
        ti = bisect.bisect_left(t, x[i])
        ans = float('inf')
        for j in range(si-1, si+1):
            for k in range(ti-1, ti+1):
                ans = min(ans, abs(s[j]-x[i])+abs(t[k]-s[j]))
                ans = min(ans, abs(t[k]-x[i])+abs(s[j]-t[k]))
        print(ans)

if __name__ == '__main__':
    main()