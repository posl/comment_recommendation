def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    # 1人あたりの平均値を求める
    ave = K // N
    # 余りを求める
    mod = K % N
    # aの中でmod以上の値の数を求める
    cnt = 0
    for i in range(N):
        if a[i] <= mod:
            cnt += 1
    # 出力
    for i in range(N):
        if a[i] <= mod:
            print(ave + 1)
        else:
            print(ave)

if __name__ == '__main__':
    main()