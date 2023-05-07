def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 200で割ったあまりの組み合わせを辞書で管理
    # key: あまり, value: そのあまりの数字のindexのリスト
    remainder = {}
    for i, a in enumerate(A):
        r = a % 200
        if r in remainder:
            print("Yes")
            print(len(remainder[r]), *remainder[r])
            print(1, i + 1)
            return
        remainder[r] = [i + 1]
    print("No")
