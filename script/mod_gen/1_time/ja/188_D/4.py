def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][1] - AB[i][0] + 1
    ans *= C
    for i in range(N):
        if i == 0:
            ans -= C
            continue
        if AB[i][0] <= AB[i - 1][1]:
            ans -= C * (AB[i - 1][1] - AB[i][0] + 1)
    print(ans)

if __name__ == '__main__':
    main()