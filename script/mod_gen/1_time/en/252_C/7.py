def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(10):
        ans = max(ans, min(sum(s[i] != s[j] for s in S) for j in range(10)))
    print(ans)

if __name__ == '__main__':
    main()