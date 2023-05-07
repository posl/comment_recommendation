def main():
    x,y,n = map(int,input().split())
    a = x
    b = y
    c = 0
    for i in range(n):
        a += x
        b += y
        if a <= b:
            c = a
        else:
            c = b
    print(c)
