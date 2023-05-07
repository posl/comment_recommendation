def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 1
    for i in range(N):
        if S[i] == 'AND':
            ans *= 2
        else:
            ans = ans * 2 + 1
    print(ans)
