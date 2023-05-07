def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 10**9
    for i in range(N):
        if X[i] - A[i] > 0:
            ans = min(ans, P[i])
    if ans == 10**9:
        ans = -1
    print(ans)
main()

if __name__ == '__main__':
    main()