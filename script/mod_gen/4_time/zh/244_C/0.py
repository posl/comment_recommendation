def main():
    n = int(input())
    a = []
    for i in range(1,2*n+2):
        a.append(i)
    judge = 0
    while(1):
        if judge == 0:
            print(a.pop(0))
            judge = 1
        elif judge == 1:
            b = int(input())
            if b == 0:
                break
            else:
                a.remove(b)
                judge = 0

if __name__ == '__main__':
    main()