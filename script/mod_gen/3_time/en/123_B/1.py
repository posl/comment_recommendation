def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a%10 == 0:
        a1 = a
    else:
        a1 = a + (10 - a%10)
    if b%10 == 0:
        b1 = b
    else:
        b1 = b + (10 - b%10)
    if c%10 == 0:
        c1 = c
    else:
        c1 = c + (10 - c%10)
    if d%10 == 0:
        d1 = d
    else:
        d1 = d + (10 - d%10)
    if e%10 == 0:
        e1 = e
    else:
        e1 = e + (10 - e%10)
    print(a1 + b1 + c1 + d1 + e1 - max(a1,b1,c1,d1,e1))

if __name__ == '__main__':
    main()