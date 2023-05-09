def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if a[0] == 1:
        if a == b:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()