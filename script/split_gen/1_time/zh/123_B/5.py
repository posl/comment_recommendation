def problem123_b():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = 0
    if a % 10 != 0:
        a = a + (10 - a % 10)
    if b % 10 != 0:
        b = b + (10 - b % 10)
    if c % 10 != 0:
        c = c + (10 - c % 10)
    if d % 10 != 0:
        d = d + (10 - d % 10)
    if e % 10 != 0:
        e = e + (10 - e % 10)
    if a >= b and a >= c and a >= d and a >= e:
        ans = ans + a
    elif b >= a and b >= c and b >= d and b >= e:
        ans = ans + b
    elif c >= a and c >= b and c >= d and c >= e:
        ans = ans + c
    elif d >= a and d >= b and d >= c and d >= e:
        ans = ans + d
    elif e >= a and e >= b and e >= c and e >= d:
        ans = ans + e
    print(ans)
