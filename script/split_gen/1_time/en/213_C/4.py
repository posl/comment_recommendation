def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    ans = []
    for i in range(N):
        ans.append([A.index(A[i])+1, B.index(B[i])+1])
    for i in range(N):
        print(ans[i][0], ans[i][1])
