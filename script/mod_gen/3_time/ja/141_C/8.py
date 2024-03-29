def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    result = [k-q for _ in range(n)]
    for i in range(q):
        result[a[i]-1] += 1
    for i in range(n):
        if result[i] <= 0:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()