def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(N):
        if i < M and BC[i][1] > A[i]:
            ans += BC[i][1]
        else:
            ans += A[i]
    print(ans)
