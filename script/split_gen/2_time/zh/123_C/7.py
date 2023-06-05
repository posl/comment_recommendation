def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a % 10 == 0:
        a = a
    else:
        a = a + (10 - a % 10)
    if b % 10 == 0:
        b = b
    else:
        b = b + (10 - b % 10)
    if c % 10 == 0:
        c = c
    else:
        c = c + (10 - c % 10)
    if d % 10 == 0:
        d = d
    else:
        d = d + (10 - d % 10)
    if e % 10 == 0:
        e = e
    else:
        e = e + (10 - e % 10)
    print(a + b + c + d + e)
