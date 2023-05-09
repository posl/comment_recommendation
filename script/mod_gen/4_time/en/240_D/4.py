def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*10**5+1)
    c = 0
    for i in a:
        b[i] += 1
        if b[i] == i:
            c += 1
        elif b[i] > i:
            b[i] = 0
    for i in a:
        if b[i] == 0:
            print(c)
        else:
            print(c+1)

if __name__ == '__main__':
    main()