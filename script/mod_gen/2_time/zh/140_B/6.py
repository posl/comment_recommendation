def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    sum = 0
    for i in range(n):
        sum += b[a[i] - 1]
        if i > 0 and a[i] == a[i - 1] + 1:
            sum += c[a[i - 1] - 1]
    print(sum)

if __name__ == '__main__':
    main()