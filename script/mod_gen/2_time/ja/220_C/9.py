def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    # 10^5回連結した数列を作成
    b = []
    for i in range(10**5):
        for j in range(n):
            b.append(a[j])
    # Bの累積和を作成
    c = [0]
    for i in range(10**5*n):
        c.append(c[i] + b[i])
    # 累積和の中でXを超える最小の値を探す
    ans = 0
    for i in range(10**5*n):
        if c[i] > x:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()