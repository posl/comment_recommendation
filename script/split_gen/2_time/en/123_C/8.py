def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if n%a == 0:
        x = n//a
    else:
        x = n//a + 1
    if n%b == 0:
        y = n//b
    else:
        y = n//b + 1
    if n%c == 0:
        z = n//c
    else:
        z = n//c + 1
    if n%d == 0:
        w = n//d
    else:
        w = n//d + 1
    if n%e == 0:
        v = n//e
    else:
        v = n//e + 1
    print(4 + max(x,y,z,w,v))
