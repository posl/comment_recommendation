def main():
    N, M = map(int, input().split())
    U = [0] * M
    V = [0] * M
    for i in range(M):
        U[i], V[i] = map(int, input().split())
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            u1 = U[i]
            v1 = V[i]
            u2 = U[j]
            v2 = V[j]
            if u1 == u2 or u1 == v2 or v1 == u2 or v1 == v2:
                continue
            if (u1 == v1 and u2 == v2) or (u1 == v2 and u2 == v1):
                continue
            if (u1 == u2 and v1 == v2):
                continue
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()