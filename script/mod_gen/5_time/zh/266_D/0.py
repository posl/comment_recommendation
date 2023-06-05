def problems266_d():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    x = 0
    t = 0
    for i in range(n):
        x1, t1, a1 = txa[i]
        x2, t2, a2 = txa[i-1]
        # 从x1 -> x2, t1 -> t2
        dt = t2 - t1
        dx = abs(x2 - x1)
        if dt < dx:
            print('No')
            return
        elif dt == dx:
            if a1 != a2:
                print('No')
                return
        else:
            if (dt - dx) % 2 == 1:
                if a1 != a2:
                    print('No')
                    return
            else:
                if a1 < a2:
                    print('No')
                    return
        x = x1
        t = t1
    print('Yes')

if __name__ == '__main__':
    problems266_d()