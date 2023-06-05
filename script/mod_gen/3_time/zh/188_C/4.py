def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 二分探索
    def bisect(l, r):
        if r - l == 1:
            return l
        else:
            m = (l + r) // 2
            l1 = bisect(l, m)
            l2 = bisect(m, r)
            if a[l1] > a[l2]:
                return l1
            else:
                return l2
    print(bisect(0, 2 ** n))

if __name__ == '__main__':
    main()