def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(N + 1)
    ans = 0
    s = 0
    for i in range(K):
        if A[i + 1] - A[i] > ans:
            ans = A[i + 1] - A[i] - 1
            s = A[i]
    print(s)
    print(ans)
    return
main()
