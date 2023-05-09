def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    if N > M:
        print('No')
        return
    i = 0
    j = 0
    while i < N and j < M:
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == N:
        print('Yes')
    else:
        print('No')
