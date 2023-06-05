def main():
    x,a,d,n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
            return
        else:
            print(1)
            return
    if n == 1:
        if x == a:
            print(0)
            return
        else:
            print(1)
            return
    if d < 0:
        d = -d
        a = -a
    if x < a:
        if (a-x) % d == 0:
            print((a-x)//d)
            return
        else:
            print((a-x)//d+1)
            return
    if x > a:
        if (x-a) % d == 0:
            print((x-a)//d)
            return
        else:
            print((x-a)//d+1)
            return
    if x == a:
        print(0)
        return
