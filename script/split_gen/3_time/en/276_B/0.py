def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        ans = 0
        for j in range(M):
            if A[j] == i+1:
                ans += 1
            elif B[j] == i+1:
                ans += 1
        print(ans)
