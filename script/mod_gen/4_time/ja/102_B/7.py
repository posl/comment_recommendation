def main():
    # 標準入力受け取り
    n = int(input())
    a = list(map(int, input().split()))
    # 絶対値の最大値を求める
    max = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(a[i]-a[j]) > max:
                max = abs(a[i]-a[j])
    # 標準出力
    print(max)

if __name__ == '__main__':
    main()