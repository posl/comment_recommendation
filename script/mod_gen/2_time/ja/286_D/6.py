def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += a[j] * b[j]
        if sum == x:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()