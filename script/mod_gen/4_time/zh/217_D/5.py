def main():
    L, Q = map(int, input().split())
    mark = [0] * (L+1)
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        elif c == 2:
            l = 0
            r = L
            while r - l > 1:
                m = (l + r) // 2
                if sum(mark[:m+1]) >= x:
                    r = m
                else:
                    l = m
            print(r)

if __name__ == '__main__':
    main()