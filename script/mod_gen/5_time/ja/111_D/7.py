def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    if n == 1:
        print(1)
        print(1)
        print("L")
        exit()
    if n == 2:
        if x[0] == x[1] and y[0] == y[1]:
            print(1)
            print(1)
            print("L")
        else:
            print(2)
            print(1, 1)
            print("RL")
            print("LR")
        exit()
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print(2)
                print(1, 1)
                print("RL")
                print("LR")
                exit()
    print(3)
    print(1, 1, 1)
    print("RLD")
    print("LDR")
    print("DRU")

if __name__ == '__main__':
    main()