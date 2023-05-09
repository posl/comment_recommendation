def main():
    N = int(input())
    A, P, X = [], [], []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    min_p = 10**9
    for i in range(N):
        if X[i] > A[i] and min_p > P[i]:
            min_p = P[i]
    if min_p == 10**9:
        print(-1)
    else:
        print(min_p)

if __name__ == '__main__':
    main()