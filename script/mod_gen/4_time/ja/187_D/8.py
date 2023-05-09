def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    aoki = sum([ab[0] for ab in AB])
    takahashi = 0
    ans = 0
    for ab in AB:
        ans += 1
        aoki -= ab[0]
        takahashi += sum(ab)
        if takahashi > aoki:
            break
    print(ans)

if __name__ == '__main__':
    main()