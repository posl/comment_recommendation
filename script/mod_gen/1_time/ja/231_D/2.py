def main():
    n, m = map(int, input().split())
    A = [0] * m
    B = [0] * m
    for i in range(m):
        A[i], B[i] = map(int, input().split())
    if m == 0:
        print('Yes')
        return
    if n == 2:
        print('No')
        return
    if n == 3:
        if m == 1:
            print('Yes')
        else:
            print('No')
        return
    if m == n - 1:
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()