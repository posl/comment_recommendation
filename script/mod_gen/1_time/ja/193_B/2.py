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
    result = -1
    for i in range(N):
        if X[i] > A[i]:
            if result == -1:
                result = P[i]
            else:
                result = min(result, P[i])
    print(result)

if __name__ == '__main__':
    main()