def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    #print(B)
    ans = [0] * N
    for i in range(N):
        if B[i] == 1:
            ans[i] = 0
        else:
            ans[i] = (B[i] * (B[i] - 1)) // 2
    #print(ans)
    for i in range(N):
        print((N - 1) * (N - 2) // 2 - ans[A[i] - 1] + 1)
