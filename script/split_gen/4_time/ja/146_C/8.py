def main():
    a, b, x = map(int, input().split())
    #print(a, b, x)
    #print(len(str(x)))
    #print(x // (a+b))
    if a + b > x:
        print(0)
    else:
        if a * (10 ** 9) + b * 10 < x:
            print(10 ** 9)
        else:
            print((x - b) // a)
    return
