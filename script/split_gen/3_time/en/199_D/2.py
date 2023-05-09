def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        E[a - 1].append(b - 1)
        E[b - 1].append(a - 1)
    ans = 0
    for i in range(3 ** N):
        color = [0] * N
        for j in range(N):
            color[j] = i // 3 ** j % 3
        is_ok = True
        for j in range(N):
            for k in E[j]:
                if color[j] == color[k]:
                    is_ok = False
        if is_ok:
            ans += 1
    print(ans)
main()
