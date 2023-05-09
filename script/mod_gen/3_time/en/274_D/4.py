def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(abs(x - y))
    for i in range(n):
        for j in range(i+1, n+1):
            if a[i] + a[j] == abs(x - y):
                print('Yes')
                return
    print('No')
main()

if __name__ == '__main__':
    main()