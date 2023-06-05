def main():
    n = int(input())
    a = 1
    b = 2*n+1
    while True:
        print(a)
        a = int(input())
        if a == 0:
            break
        if a < b:
            a,b = b,a
        b = 2*a-b-1
        if b < a:
            b,a = a,b
        if b == 0:
            break
