def main():
    n,m = map(int, input().split())
    b = []
    for i in range(n):
        b.append(list(map(int, input().split())))
    for i in range(10**100):
        a = []
        for j in range(1,8):
            a.append(i*7+j)
        if a == b[0]:
            break
    for i in range(n):
        if a != b[i]:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()