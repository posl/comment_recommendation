def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, k)
    #print(a)
    #print('')
    # 2進数表記したときの桁数を求める
    bit = 0
    for i in range(0, 60):
        if k & (1 << i) > 0:
            bit = i + 1
    #print(bit)
    # 2進数表記したときの各桁の値を求める
    b = [0] * bit
    for i in range(0, n):
        for j in range(0, bit):
            b[j] += (a[i] & (1 << j)) >> j
    #print(b)
    # K 以下の整数 X に対して、f(X) = (X XOR A_1) + (X XOR A_2) + ... + (X XOR A_N) とします。
    # 2進数表記したときの各桁の値を求める
    c = [0] * bit
    for i in range(0, n):
        for j in range(0, bit):
            if (k & (1 << j)) > 0:
                #print(i, j, b[j])
                c[j] += (n - b[j]) << j
            else:
                c[j] += b[j] << j
    #print(c)
    # c から 10 進数に変換する
    ans = 0
    for i in range(0, bit):
        ans += c[i]
    print(ans)

if __name__ == '__main__':
    main()