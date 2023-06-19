def problem123_b():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    a1 = a%10
    b1 = b%10
    c1 = c%10
    d1 = d%10
    e1 = e%10
    if a1 == 0:
        a2 = a
    else:
        a2 = a + (10 - a1)
    if b1 == 0:
        b2 = b
    else:
        b2 = b + (10 - b1)
    if c1 == 0:
        c2 = c
    else:
        c2 = c + (10 - c1)
    if d1 == 0:
        d2 = d
    else:
        d2 = d + (10 - d1)
    if e1 == 0:
        e2 = e
    else:
        e2 = e + (10 - e1)
    if a2 >= b2 and a2 >= c2 and a2 >= d2 and a2 >= e2:
        print(a2)
    elif b2 >= a2 and b2 >= c2 and b2 >= d2 and b2 >= e2:
        print(b2)
    elif c2 >= a2 and c2 >= b2 and c2 >= d2 and c2 >= e2:
        print(c2)
    elif d2 >= a2 and d2 >= b2 and d2 >= c2 and d2 >= e2:
        print(d2)
    elif e2 >= a2 and e2 >= b2 and e2 >= c2 and e2 >= d2:
        print(e2)
problem123_b()
