def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 1回目の切り込み時の角度
    theta = a[0]
    # 2回目以降の切り込み時の角度
    for i in range(1, n):
        theta += a[i]
    # 最大の角度を求める
    max_theta = 0
    for i in range(n):
        # 1回目の切り込み時の角度
        theta = a[i]
        # 2回目以降の切り込み時の角度
        for j in range(n):
            if i == j:
                continue
            theta += a[j]
        # 最大の角度を求める
        if theta > max_theta:
            max_theta = theta
    # 出力
    print(max_theta)

if __name__ == '__main__':
    main()