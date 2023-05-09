def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    b = [k-q] * n
    for i in range(q):
        b[a[i]-1] += 1
    for i in range(n):
        if b[i] > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()