def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    a.sort()
    b.sort()
    # print(a)
    # print(b)
    if a[0] == 1:
        for i in range(N-1):
            if a[i] != i+1 or b[i] != N:
                print('No')
                exit()
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()