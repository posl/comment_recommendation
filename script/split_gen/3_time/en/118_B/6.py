def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(M):
        if all(i + 1 in a for a in A):
            ans += 1
    print(ans)
