def main():
    #入力
    N, M = map(int, input().split())
    #Mの素因数分解
    p = {}
    for i in range(2, M + 1):
        while M % i == 0:
            if i in p:
                p[i] += 1
            else:
                p[i] = 1
            M //= i
        if M == 1:
            break
    #print(p)
    #N個の区別できる箱に入れる場合の数を計算
    ans = 1
    for i in p.values():
        ans *= i + 1
    #print(ans)
    #N個の区別できる箱に入れる場合の数を求める
    ans = pow(ans, N, 10**9 + 7)
    print(ans)

if __name__ == '__main__':
    main()