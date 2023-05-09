def main():
    #入力
    n = int(input())
    v = list(map(int, input().split()))
    #奇数番目と偶数番目の数列を作成
    v1 = v[::2]
    v2 = v[1::2]
    #数列の種類を調べる
    set1 = set(v1)
    set2 = set(v2)
    #数列の種類が1種類の場合
    if len(set1) == 1 and len(set2) == 1:
        #数列がすべて同じ値の場合
        if set1 == set2:
            print(0)
        #数列がすべて同じ値ではない場合
        else:
            print(2)
    #数列の種類が2種類の場合
    else:
        #数列の種類を調べる
        set1 = set(v1)
        set2 = set(v2)
        #数列の種類を調べる
        c1 = v1.count(set1.pop())
        c2 = v1.count(set1.pop())
        c3 = v2.count(set2.pop())
        c4 = v2.count(set2.pop())
        #数列の種類を調べる
        c = max(c1, c2, c3, c4)
        #数列の種類を調べる
        print(n - c)

if __name__ == '__main__':
    main()