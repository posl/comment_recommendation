def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += (a[i] - a[j]) ** 2
    print(sum)

if __name__ == '__main__':
    main()