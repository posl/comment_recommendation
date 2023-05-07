def main():
    N = int(input())
    S = [str(input()) for n in range(N)]
    ans = 0
    for i in range(10):
        t = 0
        for s in S:
            if s[i] != s[(i + 1) % 10]:
                t = max(t, i + 1)
        ans = max(ans, t)
    print(ans)
    return

if __name__ == '__main__':
    main()