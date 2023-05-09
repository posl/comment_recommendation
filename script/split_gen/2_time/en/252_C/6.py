def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(10):
        ans = max(ans, sum(S[j][i%10] != S[0][i] for j in range(N)))
    print(ans)
