def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 10**18
    for i in range(N):
        t = 0
        for j in range(N):
            d = (i - j) % N
            t += min(d, N - d)
            for k in range(10):
                if S[j][k] != S[i][(k + d) % 10]:
                    t += 1
        ans = min(ans, t)
    print(ans)
