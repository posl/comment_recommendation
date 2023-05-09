def main():
    N = int(input())
    A = list(map(int, input().split()))
    #1. Aをソートする
    A.sort()
    #2. Aの要素を集計する
    cnt = [0] * 1000000001
    for a in A:
        cnt[a] += 1
    #3. 集計した要素から組み合わせを計算する
    ans = 0
    for i in range(len(cnt)):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()