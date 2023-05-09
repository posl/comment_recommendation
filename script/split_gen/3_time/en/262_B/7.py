def main():
    N, M = map(int, input().split())
    E = [tuple(map(int, input().split())) for _ in range(M)]
    E = set(E)
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if (i, j) in E and (j, k) in E and (k, i) in E:
                    ans += 1
    print(ans)
