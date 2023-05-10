def solve():
    l, r = map(int, input().split())
    if r - l >= 2019:
        print(0)
        return
    else:
        l = l % 2019
        r = r % 2019
        if l > r:
            print(0)
            return
        else:
            m = 2019
            for i in range(l, r):
                for j in range(i+1, r+1):
                    if m > (i * j) % 2019:
                        m = (i * j) % 2019
            print(m)
            return
