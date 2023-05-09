def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1回目の操作
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[i] = A[i]
        else:
            B[i] = -A[i]
    ans = sum(B)
    # 2回目の操作
    for i in range(N):
        if i % 2 == 0:
            B[i] = -A[i]
        else:
            B[i] = A[i]
    ans = max(ans, sum(B))
    print(ans)
