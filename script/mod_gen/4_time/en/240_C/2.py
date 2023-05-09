def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    sum = 0
    for i in range(n):
        if (i+1) % 2 == 0:
            sum += a[i]
        else:
            sum += b[i]
    if sum <= x:
        print('Yes')
    else:
        print('No')
    return

if __name__ == '__main__':
    main()