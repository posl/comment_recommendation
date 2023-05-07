def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    # 約数全列挙
    def divisor(n):
        i = 1
        table = []
        while i * i <= n:
            if n % i == 0:
                table.append(i)
                if i != n // i:
                    table.append(n // i)
            i += 1
        return table
    # 約数の個数を求める
    def count_divisor(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
            i += 1
        return cnt
    # 約数の個数を求める
    def count_divisor2(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
            i += 1
        return cnt
    # 約数の個数を求める
    def count_divisor3(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
            i += 1
        return cnt
    # 約数の個数を求める
    def count_divisor4(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
            i += 1
        return cnt
    # 約数の個数を求める
    def count_divisor5(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt

if __name__ == '__main__':
    main()