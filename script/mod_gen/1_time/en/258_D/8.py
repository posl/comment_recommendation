def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # 二分探索
    left = 0
    right = 10 ** 18
    while right - left > 1:
        mid = (left + right) // 2
        # mid 分以内に X 回クリアできるか
        cnt = 0
        for a, b in AB:
            cnt += 1
            if a > mid:
                continue
            # 映像を見る回数
            cnt += (mid - a) // b
        if cnt >= X:
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()