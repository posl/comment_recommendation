def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [int(input()) for i in range(q)]
    c = [0 for i in range(n)]
    for i in range(q):
        c[l[i]-1] += 1
    for i in range(n):
        if k - q + c[i] > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()