def main():
    N, M = map(int, input().split())
    U = []
    V = []
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)
    ans = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a == b:
                continue
            for c in range(1, N + 1):
                if b == c or c == a:
                    continue
                if (a in U and b in U and c in U) or (a in V and b in V and c in V):
                    ans += 1
    print(ans // 6)
