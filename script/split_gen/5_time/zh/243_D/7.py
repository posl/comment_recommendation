def main():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'L':
            pass
        elif S[i] == 'R':
            ans += 2 ** (i + 1)
        else:
            ans -= 2 ** (i + 1)
    print(ans)
