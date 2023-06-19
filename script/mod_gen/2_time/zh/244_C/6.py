def main():
    n = int(input())
    a = 1
    b = 2*n+1
    while True:
        print(a)
        a = int(input())
        if a == 0:
            break
        print(b)
        b = int(input())
        if b == 0:
            break
        if a < b:
            a = b
        else:
            b = a
main()
