def main():
    N, X = map(int, input().split())
    burger = [1]
    for i in range(N):
        burger.append(burger[-1] * 2 + 3)
    ans = 0
    while N >= 0:
        if X > burger[N] + 1:
            ans += burger[N] + 1
            X -= burger[N] + 2
        elif X == burger[N] + 1:
            ans += 1
            break
        N -= 1
    print(ans)

if __name__ == '__main__':
    main()