def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = list(map(int, input().split()))
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 1000000000000000000
    for i in range(N):
        if X[i] > A[i]:
            ans = min(ans, P[i])
    if ans == 1000000000000000000:
        ans = -1
    print(ans)
main()

if __name__ == '__main__':
    main()