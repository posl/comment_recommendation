def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort()
    ans = 0
    for i in range(N-1):
        ans += p[i]
    ans += p[-1]//2
    print(ans)

if __name__ == '__main__':
    main()