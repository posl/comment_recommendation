def main():
    A, B, Q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        ans = 10**20
        for j in range(A+2):
            for k in range(B+2):
                if s[j] <= x[i] and x[i] <= t[k]:
                    ans = min(ans, max(x[i]-s[j], t[k]-x[i]))
                elif s[j] > x[i] and t[k] < x[i]:
                    ans = min(ans, min(x[i]-s[j], t[k]-x[i]), 2*(x[i]-s[j])+t[k]-s[j], 2*(t[k]-x[i])+t[k]-s[j])
                elif s[j] > x[i]:
                    ans = min(ans, s[j]-x[i], t[k]-s[j]+x[i]-s[j])
                elif t[k] < x[i]:
                    ans = min(ans, x[i]-t[k], t[k]-s[j]+t[k]-x[i])
        print(ans)

if __name__ == '__main__':
    main()