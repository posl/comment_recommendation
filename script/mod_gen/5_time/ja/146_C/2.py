def main():
    # A, B, X = map(int, input().split())
    # N = (X - B) // A
    # print(N if N <= 10**9 else 10**9)
    # 二分探索で解く
    A, B, X = map(int, input().split())
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        m = (l + r) // 2
        if A * m + B * len(str(m)) <= X:
            l = m
        else:
            r = m
    print(l)

if __name__ == '__main__':
    main()