def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        st = input().split()
        S.append(st[0])
        T.append(int(st[1]))
    T_max = max(T)
    T_max_idx = T.index(T_max)
    S_max = S[T_max_idx]
    T_max_idx2 = 0
    for i in range(N):
        if T[i] == T_max and S[i] == S_max:
            T_max_idx2 = i
            break
    print(T_max_idx2 + 1)
