def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, D, A)
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i]+A[j])
    #print(S)
    ans = -1
    for i in S:
        if i % D == 0:
            ans = max(ans, i)
    print(ans)

if __name__ == '__main__':
    main()