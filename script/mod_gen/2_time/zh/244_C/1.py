def main():
    n = int(input())
    a = 1
    b = 2*n
    while True:
        print(a)
        a = int(input())
        if a == 0:
            exit()
        elif a > b:
            print(a)
            exit()
        else:
            b = 2*a+1
main()
