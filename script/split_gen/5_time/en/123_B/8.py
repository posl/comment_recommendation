def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    #print(a,b,c,d,e)
    a = a % 10
    b = b % 10
    c = c % 10
    d = d % 10
    e = e % 10
    #print(a,b,c,d,e)
    if a == 0:
        a = 10
    if b == 0:
        b = 10
    if c == 0:
        c = 10
    if d == 0:
        d = 10
    if e == 0:
        e = 10
    #print(a,b,c,d,e)
    if a == 10:
        a = 0
    if b == 10:
        b = 0
    if c == 10:
        c = 0
    if d == 10:
        d = 0
    if e == 10:
        e = 0
    #print(a,b,c,d,e)
    a = a + b + c + d + e
    print(a)
    return 0
