def main():
    L, Q = map(int, input().split())
    cut = []
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            l = 0
            r = len(cut)
            while r - l > 1:
                m = (l + r) // 2
                if cut[m] < x:
                    l = m
                else:
                    r = m
            if cut[l] < x:
                print(x - cut[l])
            else:
                print(x)

if __name__ == '__main__':
    main()