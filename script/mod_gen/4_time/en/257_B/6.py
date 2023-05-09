def main():
    # input
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [int(input()) for i in range(q)]
    # compute
    points = [0] * n
    for i in range(k):
        points[a[i]-1] += 1
    for i in range(q):
        points[l[i]-1] += 1
    # output
    for i in range(n):
        if points[i] > q:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()