def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += a[i] * b[i]
    print('Yes' if s == 0 else 'No')

if __name__ == '__main__':
    main()