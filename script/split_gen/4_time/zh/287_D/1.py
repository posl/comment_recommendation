def solve():
    S = input()
    T = input()
    N = len(T)
    S = S.replace('?', '0')
    T = T.replace('?', '0')
    S = S + '0' * N
    for i in range(len(S) - N + 1):
        if S[i:i + N] == T:
            print("Yes")
        else:
            print("No")
