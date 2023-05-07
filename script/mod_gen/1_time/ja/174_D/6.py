def main():
    N = int(input())
    S = input()
    # 左からi番目までの石のうち、赤い石の個数
    red = [0]
    for s in S:
        if s == "R":
            red.append(red[-1] + 1)
        else:
            red.append(red[-1])
    ans = 10**9
    for i in range(1, N + 1):
        # 左からi番目までの白い石のうち、左隣に赤い石がある個数
        left = red[i] - 1
        # 右からi番目までの白い石のうち、右隣に赤い石がある個数
        right = N - i - (red[-1] - red[i])
        ans = min(ans, left + right)
    print(ans)

if __name__ == '__main__':
    main()