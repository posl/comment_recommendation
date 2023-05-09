def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2つの要素の中央値を求める
    def median(a, b):
        return (a + b) // 2
    # 3つの要素の中央値を求める
    def median3(a, b, c):
        if a > b:
            if c > a:
                return a
            elif c > b:
                return c
            else:
                return b
        else:
            if c > b:
                return b
            elif c > a:
                return c
            else:
                return a
    # 単純な中央値を求める
    def simple_median(a, b, c):
        if a > b:
            if c > a:
                return a
            elif c > b:
                return c
            else:
                return b
        else:
            if c > b:
                return b
            elif c > a:
                return c
            else:
                return a
    # 3つの要素の中央値を求める(別解)
    def median3_2(a, b, c):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        return b
    # 3つの要素の中央値を求める(別解)
    def median3_3(a, b, c):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        return b
    # 3つの要素の中央値を求める(別解)
    def median3_4(a, b, c):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        return b
    # 3つの要素の中央値を求める(別解)
    def

if __name__ == '__main__':
    main()