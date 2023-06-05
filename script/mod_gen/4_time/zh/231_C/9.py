def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        num = 0
        for j in range(n):
            if a[j] >= x[i]:
                num = n - j
                break
        print(num)

if __name__ == '__main__':
    main()