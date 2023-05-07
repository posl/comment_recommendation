def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    s = []
    t = []
    for i in range(H):
        s.append(set([S[i][j] for j in range(W)]))
        t.append(set([T[i][j] for j in range(W)]))
    for i in range(H):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")
