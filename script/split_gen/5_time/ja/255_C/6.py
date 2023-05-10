def main():
    x,a,d,n = map(int, input().split())
    if d == 0:
        if x < a:
            print(a-x)
        else:
            print(x-a)
    else:
        if n % 2 == 0:
            if x < a:
                print(a-x)
            else:
                print(x-a)
        else:
            if x < a:
                if (a-x) % d == 0:
                    print((a-x)//d)
                else:
                    print((a-x)//d + 1)
            else:
                if (x-a) % d == 0:
                    print((x-a)//d)
                else:
                    print((x-a)//d + 1)
