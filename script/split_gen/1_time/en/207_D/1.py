def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a, b = map(int, input().split())
        S.append((a, b))
    for i in range(N):
        c, d = map(int, input().split())
        T.append((c, d))
    # Sを回転させてTに一致するか
    for i in range(4):
        if S == T:
            print('Yes')
            exit()
        S = [(b, -a) for a, b in S]
    # Sを平行移動させてTに一致するか
    for i in range(N):
        dx = T[i][0] - S[0][0]
        dy = T[i][1] - S[0][1]
        S2 = [(a + dx, b + dy) for a, b in S]
        if S2 == T:
            print('Yes')
            exit()
    print('No')
