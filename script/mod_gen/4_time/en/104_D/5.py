def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    A = 0
    B = 0
    C = 0
    Q = 0
    for i in range(N):
        if S[i] == 'A':
            A += 1
        elif S[i] == 'B':
            B += 1
        elif S[i] == 'C':
            C += 1
        else:
            Q += 1
    ABC = A * B * C
    ABC2 = ABC * pow(3, Q, MOD) % MOD
    ABC3 = ABC2 * pow(3, MOD - 2, MOD) % MOD
    ABC4 = ABC3 * pow(3, MOD - 2, MOD) % MOD
    ABC5 = ABC4 * pow(3, MOD - 2, MOD) % MOD
    ABC6 = ABC5 * pow(3, MOD - 2, MOD) % MOD
    ABC7 = ABC6 * pow(3, MOD - 2, MOD) % MOD
    ABC8 = ABC7 * pow(3, MOD - 2, MOD) % MOD
    ABC9 = ABC8 * pow(3, MOD - 2, MOD) % MOD
    ABC10 = ABC9 * pow(3, MOD - 2, MOD) % MOD
    ABC11 = ABC10 * pow(3, MOD - 2, MOD) % MOD
    ABC12 = ABC11 * pow(3, MOD - 2, MOD) % MOD
    ABC13 = ABC12 * pow(3, MOD - 2, MOD) % MOD
    ABC14 = ABC13 * pow(3, MOD - 2, MOD) % MOD
    ABC15 = ABC14 * pow(3, MOD - 2, MOD) % MOD
    ABC16 = ABC15 * pow(3, MOD - 2, MOD) % MOD
    ABC17 = ABC16 * pow(3, MOD - 2, MOD) % MOD
    ABC18 = ABC17 * pow(3, MOD - 2, MOD) % MOD
    ABC19 = ABC18 * pow(3, MOD - 2, MOD) % MOD
    ABC20 = ABC19 * pow

if __name__ == '__main__':
    main()