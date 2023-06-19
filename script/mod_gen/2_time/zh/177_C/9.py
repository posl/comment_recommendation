def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += a[i] * a[j]
    print(sum % (10**9+7))

if __name__ == '__main__':
    main()