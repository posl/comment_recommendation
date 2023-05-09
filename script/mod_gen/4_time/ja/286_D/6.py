def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    # print(n, x)
    # print(a)
    # print(b)
    # print(sum([a[i] * b[i] for i in range(n)]))
    if sum([a[i] * b[i] for i in range(n)]) >= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()