def solve():
    S = input()
    MOD = 10**9 + 7
    C = [0] * 8
    C[0] = 1
    for s in S:
        if s == 'c':
            C[1] += C[0]
        elif s == 'h':
            C[2] += C[1]
        elif s == 'o':
            C[3] += C[2]
        elif s == 'k':
            C[4] += C[3]
        elif s == 'u':
            C[5] += C[4]
        elif s == 'd':
            C[6] += C[5]
        elif s == 'a':
            C[7] += C[6]
        elif s == 'i':
            C[0] += C[7]
        for i in range(8):
            C[i] %= MOD
    print(C[0])

if __name__ == '__main__':
    solve()