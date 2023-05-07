def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    ans = sum(p[0:N-1]) + p[N-1] // 2
    print(ans)

if __name__ == '__main__':
    main()