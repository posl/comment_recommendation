def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i, n, i+1):
            sum += b[j]
        if sum%2 != a[i]:
            b[i] = 1
    print(sum(b))
    for i in range(n):
        if b[i] == 1:
            print(i+1, end=' ')
    print()

if __name__ == '__main__':
    main()