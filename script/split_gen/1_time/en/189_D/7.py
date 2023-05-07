def main():
    N = int(input())
    s = [input() for _ in range(N)]
    ans = 2 ** N
    for i in range(N):
        if s[i] == 'AND':
            ans -= 2 ** (N - i - 1)
    print(ans)
