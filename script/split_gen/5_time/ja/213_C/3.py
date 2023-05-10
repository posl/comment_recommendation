def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [[0 for j in range(2)] for i in range(N)]
    for i in range(N):
        ans[i][0] = A[i]
        ans[i][1] = B[i]
    ans.sort(key=lambda x: x[0] + x[1])
    for i in range(N):
        print(ans[i][0], ans[i][1])
