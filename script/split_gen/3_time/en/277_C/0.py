def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 1
    for i in range(N-1, -1, -1):
        if ans % A[i] == 0:
            ans += B[i] - A[i]
        else:
            ans += B[i] - (ans % A[i])
    print(ans)
