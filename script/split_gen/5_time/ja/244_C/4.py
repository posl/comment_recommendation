def main():
    n = int(input())
    a = 1
    b = 2*n+1
    while True:
        print(a)
        a = int(input())
        if a == 0:
            exit()
        if a > b:
            print(0)
            exit()
        print(b)
        b = int(input())
        if b == 0:
            exit()
        if b < a:
            print(0)
            exit()
