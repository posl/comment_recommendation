def main():
    A, B, Q = list(map(int, input().split()))
    s = [-10**11] + [int(input()) for _ in range(A)] + [10**11]
    t = [-10**11] + [int(input()) for _ in range(B)] + [10**11]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        ans = 10**20
        for j in range(A+2):
            if s[j] > x[i]:
                break
        for k in range(B+2):
            if t[k] > x[i]:
                break
        for l in range(j-1, j+1):
            for m in range(k-1, k+1):
                ans = min(ans, max(s[l]-x[i], x[i]-t[m]))
                ans = min(ans, max(t[m]-x[i], x[i]-s[l]))
        print(ans)

if __name__ == '__main__':
    main()