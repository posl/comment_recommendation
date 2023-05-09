def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 机Aの本を読むのにかかる時間の累積和
    a_sum = [0]
    for i in a:
        a_sum.append(a_sum[-1] + i)
    # 机Bの本を読むのにかかる時間の累積和
    b_sum = [0]
    for i in b:
        b_sum.append(b_sum[-1] + i)
    # 机Aの本を読むのにかかる時間の累積和のうち、k分以内に読むことができる本の最大数
    max_a = 0
    for i in range(n+1):
        if a_sum[i] > k:
            break
        max_a = i
    # 机Bの本を読むのにかかる時間の累積和のうち、k分以内に読むことができる本の最大数
    max_b = 0
    for i in range(m+1):
        if b_sum[i] > k:
            break
        max_b = i
    # 机Aの本を読むのにかかる時間の累積和のうち、k分以内に読むことができる本の最大数と、
    # 机Bの本を読むのにかかる時間の累積和のうち、k分以内に読むことができる本の最大数の合計が最大となるものを探索する
    ans = 0
    for i in range(max_a+1):
        for j in range(max_b+1):
            if a_sum[i] + b_sum[j] <= k:
                ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    main()