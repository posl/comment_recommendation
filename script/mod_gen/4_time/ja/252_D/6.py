def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += (a[i] * a[j]) % 1000000007
    print(sum % 1000000007)

if __name__ == '__main__':
    main()