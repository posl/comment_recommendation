def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(M):
        for j in range(N):
            if i + 1 not in A[j][1:]:
                break
        else:
            ans += 1
    print(ans)
