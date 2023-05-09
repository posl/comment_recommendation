def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    pow3Q = pow(3, Q, MOD)
    ans = 0
    for i in range(pow3Q):
        T = S
        for j in range(Q):
            if i >> j & 1:
                T = T.replace('?', 'A', 1)
            elif i >> j & 2:
                T = T.replace('?', 'B', 1)
            else:
                T = T.replace('?', 'C', 1)
        ans = (ans + ABCnumber(T)) % MOD
    print(ans)
