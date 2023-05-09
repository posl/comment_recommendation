def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for a,b in AB:
        ans += a/b
    ans /= 2
    print(ans)

if __name__ == '__main__':
    main()