def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    # print(AB)
    ans = 0
    for i, (a, b) in enumerate(AB):
        if X > 0:
            ans += a + b
            X -= 1
        else:
            ans += b
    print(ans)

if __name__ == '__main__':
    main()