def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    S = [0]
    for i in range(N):
        S.append(S[i]+A[i])
    if S[K] < D:
        print(-1)
    else:
        print(S[K]//D*D)

if __name__ == '__main__':
    main()