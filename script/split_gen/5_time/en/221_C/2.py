def main():
    N = input()
    N = ''.join(sorted(N, reverse=True))
    ans = 0
    for i in range(1, len(N)):
        ans = max(ans, int(N[:i]) * int(N[i:]))
    print(ans)
