def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    A.sort()
    for i in range(Q):
        cnt = 0
        for j in range(N):
            if A[j] >= X[i]:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()