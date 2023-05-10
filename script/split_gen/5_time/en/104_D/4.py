def main():
    S = input()
    Q = S.count('?')
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    mod = 10**9 + 7
    ans = 0
    for i in range(Q+1):
        for j in range(Q+1):
            if i + j > Q:
                continue
            k = Q - i - j
            t = 1
            for _ in range(i):
                t = t * (A + _ + 1) % mod
            for _ in range(j):
                t = t * (B + _ + 1) % mod
            for _ in range(k):
                t = t * (C + _ + 1) % mod
            ans = (ans + t) % mod
    print(ans)
