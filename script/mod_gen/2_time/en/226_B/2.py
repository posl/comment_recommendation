def main():
    N = int(input())
    D = dict()
    for _ in range(N):
        A = list(map(int, input().split()))
        L = A[0]
        A = A[1:]
        if L not in D:
            D[L] = dict()
        if tuple(A) not in D[L]:
            D[L][tuple(A)] = 1
        else:
            D[L][tuple(A)] += 1
    ans = 0
    for L in D:
        ans += len(D[L])
    print(ans)
main()
