def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    from collections import Counter
    s_cnt = Counter()
    t_cnt = Counter()
    for i in range(H):
        s_cnt[S[i]] += 1
        t_cnt[T[i]] += 1
    if s_cnt != t_cnt:
        print("No")
        exit()
    s = [[] for _ in range(H)]
    t = [[] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            s[i].append(S[i][j])
            t[i].append(T[i][j])
    s.sort()
    t.sort()
    for i in range(H):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")
