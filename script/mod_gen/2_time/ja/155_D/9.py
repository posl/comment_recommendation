def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #0がある場合は、0を含む組み合わせは全て0になる
    if 0 in a:
        print(0)
        return
    #0がない場合は、最小値が負の場合は0になる
    if a[0] < 0:
        #負の値の組み合わせは、最小値と最大値の積が0になる
        if a[0] * a[-1] >= 0:
            print(0)
            return
    #負の値の組み合わせが存在する場合は、最小値の組み合わせのみを考慮する
    #0がある場合は、0を含む組み合わせは全て0になる
    #0がない場合は、最小値が負の場合は0になる
    #その他は、最小値が正の場合は、最小値の組み合わせのみを考慮する
    #print(a)
    #print(a[0])
    #print(a[-1])
    #print(a[0] * a[-1])
    #負の値の組み合わせのみを考慮
    if a[0] < 0:
        #print("負の値の組み合わせのみを考慮")
        a = a[:a.index(0)]
    #print(a)
    #積の最小値を求める
    #積の最大値は、最大値の組み合わせのみを考慮
    #print(a)
    #print(a[0])
    #print(a[-1])
    #print(a[0] * a[-1])
    #積の最大値を求める
    #積の

if __name__ == '__main__':
    main()