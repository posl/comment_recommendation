def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        if x % a[i] == 0:
            if x // a[i] <= b[i]:
                print('Yes')
                exit()
        else:
            if x // a[i] < b[i]:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()