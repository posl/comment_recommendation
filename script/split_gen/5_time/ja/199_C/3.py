def main():
    # input
    N = int(input())
    S = input()
    Q = int(input())
    TABs = [list(map(int, input().split())) for _ in range(Q)]
    # compute
    S = list(S)
    for TAB in TABs:
        if TAB[0] == 1:
            S[TAB[1]-1], S[TAB[2]-1] = S[TAB[2]-1], S[TAB[1]-1]
        else:
            S[:N], S[N:] = S[N:], S[:N]
    # output
    print(''.join(S))
