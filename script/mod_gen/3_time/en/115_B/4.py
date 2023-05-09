def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    ans = p[-1] // 2
    for i in range(n - 1):
        ans += p[i]
    print(ans)

if __name__ == '__main__':
    main()