def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 余りを格納するリスト
    remainder = [0] * 200
    # 余りを計算
    for i in range(N):
        remainder[A[i] % 200] += 1
    # 余りが2以上のものを計算
    count = 0
    for i in range(200):
        if remainder[i] >= 2:
            count += remainder[i] * (remainder[i] - 1) // 2
    print(count)

if __name__ == '__main__':
    main()