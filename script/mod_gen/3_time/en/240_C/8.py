def main():
    n, x = map(int, input().split())
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    for i in range(n):
        if x <= a[i]:
            x = a[i]
        elif x <= b[i]:
            x = b[i]
    print('Yes' if x == x else 'No')

if __name__ == '__main__':
    main()