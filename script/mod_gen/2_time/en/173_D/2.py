def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n-2):
        sum += a[i]
    print(sum)

if __name__ == '__main__':
    main()