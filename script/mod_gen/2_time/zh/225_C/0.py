def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    if a[0] == 1 and b.count(n) == n-1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()