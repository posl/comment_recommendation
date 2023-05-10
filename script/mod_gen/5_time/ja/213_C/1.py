def main():
    H, W, N = map(int, input().split())
    card = []
    for i in range(N):
        A, B = map(int, input().split())
        card.append((A, B, i + 1))
    card.sort(key=lambda x: (x[0], x[1], x[2]))
    ans = [0] * N
    for i in range(N):
        ans[i] = [card[i][0], card[i][1], card[i][2]]
    for i in range(N - 1, 0, -1):
        if ans[i][0] == ans[i - 1][0]:
            ans[i][0] = ans[i - 1][0]
            ans[i][1] = ans[i - 1][1]
        else:
            ans[i][0] = ans[i - 1][0]
            ans[i][1] = ans[i - 1][1] + 1
    for i in range(N):
        print(ans[i][0], ans[i][1])
    return

if __name__ == '__main__':
    main()