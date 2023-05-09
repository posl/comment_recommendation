def main():
    x = input()
    m = int(input())
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        return
    #二分探索
    def check(n):
        #Xをn進数としてみなす
        tmp = 0
        for i in range(len(x)):
            tmp += int(x[-1-i]) * n ** i
        if tmp <= m:
            return True
        else:
            return False
    #条件を満たす最大のnを二分探索で求める
    #nはd+1以上となる
    l = d+1
    r = 10 ** 18 + 1
    while r - l > 1:
        c = (l+r)//2
        if check(c):
            l = c
        else:
            r = c
    print(l - d)
    return

if __name__ == '__main__':
    main()