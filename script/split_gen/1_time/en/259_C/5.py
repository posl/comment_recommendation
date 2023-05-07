def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    if N > M:
        print('No')
        return
    for i in range(M - N + 1):
        s = S
        t = T[i:i + N]
        for j in range(N):
            if s[j] != t[j] and s[j] != '?':
                break
        else:
            print('Yes')
            return
    print('No')
