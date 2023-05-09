def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, M+1):
        if all(i in A[j][1:] for j in range(N)):
            ans += 1
    print(ans)
