def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a%10 == 0:
        pass
    else:
        a = (a//10+1)*10
    if b%10 == 0:
        pass
    else:
        b = (b//10+1)*10
    if c%10 == 0:
        pass
    else:
        c = (c//10+1)*10
    if d%10 == 0:
        pass
    else:
        d = (d//10+1)*10
    if e%10 == 0:
        pass
    else:
        e = (e//10+1)*10
    print(a+b+c+d+e)

if __name__ == '__main__':
    main()