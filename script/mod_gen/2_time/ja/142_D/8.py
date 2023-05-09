def main():
    A, B = map(int, input().split())
    # 約数を求める
    def divisor(n):
        i = 1
        res = []
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
            i += 1
        return res
    # AとBの約数の中で、AとBの最大公約数を含むものを求める
    res = divisor(A)
    res = [i for i in res if B % i == 0]
    # 最大公約数を除く
    res.remove(gcd(A, B))
    print(len(res))

if __name__ == '__main__':
    main()