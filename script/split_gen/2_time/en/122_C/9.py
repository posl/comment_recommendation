def main():
    N, Q = map(int, input().split())
    S = input()
    #N, Q = 8, 3
    #S = 'ACACTACG'
    #lrs = [[3, 7], [2, 3], [1, 8]]
    lrs = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(S)
    #print(lrs)
    ac = [0] * N
    for i in range(N - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            ac[i + 1] = ac[i] + 1
        else:
            ac[i + 1] = ac[i]
    #print(ac)
    for l, r in lrs:
        print(ac[r - 1] - ac[l - 1])
