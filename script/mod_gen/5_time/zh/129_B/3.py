def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 1000
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        ans = min(ans, abs(s1-s2))
    print(ans)

if __name__ == '__main__':
    main()