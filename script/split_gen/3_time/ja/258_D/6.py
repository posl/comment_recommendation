def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**18
    for i in range(N):
        a, b = AB[i]
        ans = min(ans, a*X+b*(N-i-1))
    print(ans)
