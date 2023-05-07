def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        A.sort(key=lambda x: sum([(-1)**(i>>j&1)*x[j] for j in range(3)]), reverse=True)
        ans = max(ans, sum([sum([(-1)**(i>>j&1)*A[k][j] for j in range(3)]) for k in range(M)]))
    print(ans)
