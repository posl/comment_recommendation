def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 360度の中で最も大きな角度
    max_angle = 0
    # 360度の中で最も小さな角度
    min_angle = 360
    for i in range(N):
        # 360度の中で最も大きな角度の更新
        max_angle = max(max_angle, A[i])
        # 360度の中で最も小さな角度の更新
        min_angle = min(min_angle, A[i])
    # 最も大きなピザの中心角
    max_pizza_angle = 360 - (max_angle - min_angle)
    print(max_pizza_angle)

if __name__ == '__main__':
    main()