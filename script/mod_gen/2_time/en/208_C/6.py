def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] = K//N
        if K%N > i:
            ans[i] += 1
    for i in range(N):
        if A[i] <= K%N:
            ans[i] += 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()