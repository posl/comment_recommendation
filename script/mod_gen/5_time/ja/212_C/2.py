def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # a, b をソート
    a.sort()
    b.sort()
    # a, b の要素の差の絶対値の最小値を求める
    ans = 10**9
    i = 0
    j = 0
    while i < n and j < m:
        ans = min(ans, abs(a[i]-b[j]))
        if a[i] > b[j]:
            j += 1
        else:
            i += 1
    print(ans)

if __name__ == '__main__':
    main()