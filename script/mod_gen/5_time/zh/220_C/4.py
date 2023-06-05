def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = []
    for i in range(100):
        for j in range(n):
            b.append(a[j])
    sum = 0
    k = 0
    while sum <= x:
        sum += b[k]
        k += 1
    print(k)

if __name__ == '__main__':
    main()