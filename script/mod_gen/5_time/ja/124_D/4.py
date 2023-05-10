def main():
    n, k = map(int, input().split())
    s = input()
    # 0の数をカウント
    zero_count = 0
    # 0の数をカウントするリスト
    zero_count_list = []
    # 0をカウントしていく
    for i in range(n):
        if s[i] == "0":
            zero_count += 1
        else:
            zero_count_list.append(zero_count)
            zero_count = 0
    zero_count_list.append(zero_count)
    # 0をカウントするリストを作成
    zero_count_list.sort(reverse=True)
    # 0をカウントするリストの先頭からk個の合計値を求める
    ans = 0
    for i in range(k):
        ans += zero_count_list[i]
    print(ans)

if __name__ == '__main__':
    main()