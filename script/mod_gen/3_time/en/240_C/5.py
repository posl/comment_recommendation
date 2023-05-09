def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        if X >= a[i]:
            X -= a[i]
        elif X >= b[i]:
            X -= b[i]
    if X == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()