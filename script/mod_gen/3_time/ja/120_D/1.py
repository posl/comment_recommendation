def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.reverse()
    B.reverse()
    union = UnionFind(N)
    ans = [0] * M
    for i in range(M):
        ans[i] = union.size(A[i] - 1) * union.size(B[i] - 1)
        union.union(A[i] - 1, B[i] - 1)
    ans.reverse()
    for i in range(M):
        ans[i] -= union.size(A[i] - 1) * union.size(B[i] - 1)
    for i in range(M):
        ans[i] += ans[i - 1]
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()