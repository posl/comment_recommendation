def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    aoki = sum(x[0] for x in AB)
    takahashi = 0
    ans = 0
    for i in range(N):
        aoki -= AB[i][0]
        takahashi += sum(AB[i])
        ans += 1
        if takahashi > aoki:
            break
    print(ans)

if __name__ == '__main__':
    main()