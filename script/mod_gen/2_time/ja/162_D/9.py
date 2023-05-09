def main():
    n = int(input())
    s = input()
    # 各文字の個数をカウント
    cnt = [0, 0, 0]
    for i in range(n):
        if s[i] == 'R':
            cnt[0] += 1
        elif s[i] == 'G':
            cnt[1] += 1
        else:
            cnt[2] += 1
    # 各文字の個数の組み合わせを計算
    ans = cnt[0] * cnt[1] * cnt[2]
    # 3文字の組み合わせを計算
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                continue
            if j + (j - i) < n and s[j] != s[j + (j - i)]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()