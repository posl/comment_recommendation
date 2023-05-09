def solve():
    N, A, B = map(int, input().split())
    S = input()
    for i in range(N//2):
        if S[i] != S[-i-1]:
            if S[i] == 'a':
                S = S[:i] + S[-i-1] + S[i+1:]
                A -= 1
            elif S[-i-1] == 'a':
                S = S[:i] + S[-i-1] + S[i+1:]
                A -= 1
            elif S[i] > S[-i-1]:
                S = S[:i] + S[-i-1] + S[i+1:]
                B -= 1
            else:
                S = S[:i] + S[-i-1] + S[i+1:]
                B -= 1
        if A < 0 or B < 0:
            return -1
    if N%2 == 1:
        if A > 0:
            S = S[:N//2] + 'a' + S[N//2+1:]
        elif B > 0:
            S = S[:N//2] + 'a' + S[N//2+1:]
        else:
            S = S[:N//2] + S[N//2] + S[N//2+1:]
    return A + B, S

if __name__ == '__main__':
    solve()