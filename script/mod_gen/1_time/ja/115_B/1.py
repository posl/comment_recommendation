def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    ans = 0
    for i in range(N-1):
        ans += p[i]
    ans += p[N-1] / 2
    print(int(ans))
main()

if __name__ == '__main__':
    main()