def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    if sum(a) < s:
        print('No')
        return
    else:
        print('Yes')
    sum_a = 0
    sum_b = 0
    for i in range(n):
        if sum_a + a[i] < s:
            print('H', end='')
            sum_a += a[i]
        else:
            print('T', end='')
            sum_b += b[i]
    print()
    return

if __name__ == '__main__':
    main()