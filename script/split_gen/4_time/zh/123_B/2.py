def problems123_b():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a%10==0:
        a=a
    else:
        a=a+(10-a%10)
    if b%10==0:
        b=b
    else:
        b=b+(10-b%10)
    if c%10==0:
        c=c
    else:
        c=c+(10-c%10)
    if d%10==0:
        d=d
    else:
        d=d+(10-d%10)
    if e%10==0:
        e=e
    else:
        e=e+(10-e%10)
    if a>=b and a>=c and a>=d and a>=e:
        print(a)
    elif b>=a and b>=c and b>=d and b>=e:
        print(b)
    elif c>=a and c>=b and c>=d and c>=e:
        print(c)
    elif d>=a and d>=b and d>=c and d>=e:
        print(d)
    else:
        print(e)
problems123_b()
