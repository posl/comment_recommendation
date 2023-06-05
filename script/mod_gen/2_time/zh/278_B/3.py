def main():
    a = []
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end = ' ')

if __name__ == '__main__':
    main()