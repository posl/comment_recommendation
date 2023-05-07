def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    #辞書順を定義する
    def comp(a, b):
        for i in range(min(len(a),len(b))):
            if X.index(a[i]) < X.index(b[i]):
                return -1
            elif X.index(a[i]) > X.index(b[i]):
                return 1
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        return 0
    #辞書順でソート
    S.sort(key=functools.cmp_to_key(comp))
    print(*S, sep='
')

if __name__ == '__main__':
    main()