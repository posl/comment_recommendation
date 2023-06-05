def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        T.append(int(t))
        S.append(s)
    max_t = max(T)
    max_s = []
    for i in range(N):
        if T[i] == max_t:
            max_s.append(S[i])
    if len(max_s) == 1:
        print(S.index(max_s[0])+1)
    else:
        min_i = N
        for i in range(len(max_s)):
            if S.index(max_s[i]) < min_i:
                min_i = S.index(max_s[i])
        print(min_i+1)
