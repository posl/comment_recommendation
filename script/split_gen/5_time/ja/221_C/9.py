def main():
    N = input()
    ans = 0
    for i in range(1, len(N)):
        ans = max(ans, (int(N[:i]) * int(N[i:])))
    print(ans)
