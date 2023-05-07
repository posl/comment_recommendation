def solve():
    N, M = map(int, input().split())
    if M % 2 == 1:
        print("No")
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    print("Yes")
    print(*[b + 1 for b in G[0]], sep = "
")
    return

if __name__ == '__main__':
    solve()