def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    # 2次元配列を作る
    # 0を作る
    arr = [[0 for i in range(n+1)] for j in range(n+1)]
    # 1を作る
    for i in range(n):
        arr[i+1][a[i]] = 1
    # 累積和をとる
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] += arr[i][j-1]
    # クエリの個数分ループ
    for i in range(q):
        l, r, x = map(int, input().split())
        print(arr[r][x] - arr[l-1][x])

if __name__ == '__main__':
    main()