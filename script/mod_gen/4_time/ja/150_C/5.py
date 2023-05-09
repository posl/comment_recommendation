def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    # 順列の辞書順での番号を求める
    def get_num(l):
        num = 0
        for i in range(n):
            num += l[i] * (n-i) * (n-i-1) // 2
        return num
    print(abs(get_num(p) - get_num(q)))

if __name__ == '__main__':
    main()